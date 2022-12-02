from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import GenderPet
from groups.models import Group
from traits.models  import Trait
from pets.models import Pet

import ipdb

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=GenderPet.choices, default= GenderPet.NOTINFORMED)
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    traits_count = serializers.SerializerMethodField()

    def get_traits_count(self, obj):
        trait = Trait.objects.filter(pets = obj.id)
        return len(trait)
        
    def create(self, validated_data):
        group_dict = validated_data.pop("group")
        traits_dict = validated_data.pop("traits")
        
        group = Group.objects.get_or_create(**group_dict)[0]
        
        pet = Pet.objects.create(**validated_data, group = group)
        
        for trait in traits_dict:
            traits = Trait.objects.get_or_create(**trait)[0]
            pet.traits.add(traits)
        

        return pet

    def update(self, instance, validated_data):
        try:
            traits_dict = validated_data.pop("traits")
            for trait in traits_dict:
                traits = Trait.objects.get_or_create(**trait)[0]
                instance.traits.add(traits)
        except KeyError:
            pass

        try:
            group_dict = validated_data.pop("group")
            group = Group.objects.get_or_create(**group_dict)[0]

            instance.group = group
        except KeyError:
            pass

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
