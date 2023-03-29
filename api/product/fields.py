from django.db import models
from django.core import checks
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

#!OrderField
class OrderField(models.PositiveIntegerField):
    description = "Orderinng field on a unique field"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [*super().check(**kwargs), *self._check_for_field_attribute(**kwargs)]

    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must be define a 'unique_for_field' attribute")
            ]
        elif self.unique_for_field not in [
            f.name for f in self.model._meta.get_fields()
        ]:
            return [checks.Error("OrderField does not match model field value")]
        return []

    def pre_save(self, instance, add):
        print("Instance is ", instance)
        if getattr(instance, self.attname) is None:
            print("Instance is ", instance)
            print("Attribute Value ", self.attname)
            print("Model Instance Is ", getattr(instance, self.unique_for_field))
            qs = self.model.objects.all()
            print("Model is ", self.model)
            try:
                query = {
                    self.unique_for_field: getattr(instance, self.unique_for_field)
                }
                print("Query value is ", query)
                print("Qs value is ", qs)
                new_qs = qs.filter(**query)  # return productline associated product
                print("New Qs value is ", new_qs)
                last_item = new_qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1
            return value
        else:
            print("Add value is ", add)
            query = {self.unique_for_field: getattr(instance, self.unique_for_field)}
            qs = self.model.objects.all()
            new_qs = qs.filter(**query)
            print("Query value is dam dam", query)
            print("New query value is ", new_qs)
            return super().pre_save(instance, add)

    # ?Debugging Area
    # def pre_save(self, instance, created):
    #     if getattr(instance, self.attname) is None:
    #         print("Hello")
    #         print("Attribute value ", self.attname)
    #         print("Instance Is ", instance)
    #         print("Model is ", self.model)
    #         print("Uniqie field ", self.unique_for_field)
    #         print("What is this ", getattr(instance, self.unique_for_field))
    #         a = 12
    #         return a
    #     print("instanc is ", instance)
    #     print("what happen here")

    #     return super().pre_save(instance, created)
