from textwrap import indent

from django.core.management.base import BaseCommand, no_translations

from djchoices import DjangoChoices


def get_subclasses(cls):
    for subclass in cls.__subclasses__():
        yield from get_subclasses(subclass)
        yield subclass


def iter_django_choices():
    for cls in get_subclasses(DjangoChoices):
        yield cls


BASE_CLS = {
    str: "models.TextChoices",
    int: "models.IntegerChoices",
}


class Command(BaseCommand):
    help = "Introspect DjangoChoices subclasses and generate equivalent native Django choices code."

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-wrap-gettext",
            dest="wrap_gettext",
            action="store_false",
            help="Do not wrap labels in gettext/gettext_lazy calls. See also --gettext-alias.",
        )
        parser.add_argument(
            "--gettext-alias",
            default="_",
            help="Alias/function name for the gettext(_lazy) wrapper. Defaults to '_'.",
        )

    @no_translations
    def handle(self, **options):
        wrap_gettext = options["wrap_gettext"]
        gettext_alias = options["gettext_alias"]

        def wrap_label(label):
            if not wrap_gettext:
                return label
            return f"{gettext_alias}({label})"

        for cls in iter_django_choices():
            full_path = f"{cls.__module__}.{cls.__qualname__}"

            value_types = set(
                [type(choice_item.value) for choice_item in cls._fields.values()]
            )
            if len(value_types) != 1:
                self.stdout.write(
                    f"  Choices do not have consistent value types: {value_types}"
                )
                continue

            value_type = list(value_types)[0]
            base = BASE_CLS.get(value_type)
            if not base:
                self.stdout.write(
                    indent(
                        f"No builtin enum for type '{value_type}'. You may need to define your own."
                        "See: https://docs.djangoproject.com/en/3.2/ref/models/fields/#enumeration-types",
                        prefix="  ",
                    )
                )
                continue

            lines = [
                f"# {full_path}",
                f"class {cls.__name__}({base}):",
            ]
            for field_name, choice_item in cls._fields.items():
                label = wrap_label(f'"{choice_item.label}"')
                lines.append(
                    indent(
                        f"{field_name} = {repr(choice_item.value)}, {label}",
                        prefix="    ",
                    )
                )
            snippet = indent("\n".join(lines), prefix="  ")
            self.stdout.write("\n")
            self.stdout.write(snippet)
            self.stdout.write("\n")
