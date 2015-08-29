def test_deconstructible_validator(self):
    from django.db import models

    class MyModel(models.Model):
        choice = models.CharField(choices=NumericTestClass.choices, validators=[NumericTestClass.validator])


    import pdb; pdb.set_trace()
