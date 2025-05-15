from rest_framework import serializers
from .models import *




class VokalatnamaSerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VokalatnamaSerial
        fields = ['from_serial', 'to_serial', 'total']



class VokalatnamaSalesSerializer(serializers.ModelSerializer):
    serials = VokalatnamaSerialSerializer(many=True)

    class Meta:
        model = Vokalatnama
        fields = [
            'id', 'receipt_no', 'sales_date', 'advocate_name', 'advocateId',
            'building_name', 'address', 'customer_phone', 'customer_name',
            'customer_address', 'total_count', 'total_amount', 'serials'
        ]

    def create(self, validated_data):
        # print(validated_data)
        serials_data = validated_data.pop('serials')
        print(serials_data)
        sale = Vokalatnama.objects.create(**validated_data)
        for serial_data in serials_data:
            VokalatnamaSerial.objects.create(sale=sale, **serial_data)
        return sale
    

    def update(self, instance, validated_data):
        serials_data = validated_data.pop('serials', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if serials_data is not None:
            instance.serials.all().delete()
            for serial_data in serials_data:
                VokalatnamaSerial.objects.create(sale=instance, **serial_data)

        return instance
    




class BailbondSerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BailbondSerial
        fields = ['from_serial', 'to_serial', 'total']



class BailbondSalesSerializer(serializers.ModelSerializer):
    bailbond_serials = BailbondSerialSerializer(many=True)

    class Meta:
        model = Bailbond
        fields = ['id', 'receipt_no', 'sales_date','building_name','remarks','bailbond_serials']

    def create(self, validated_data):
        serials_data = validated_data.pop('bailbond_serials')
        print(serials_data)
        sale = Vokalatnama.objects.create(**validated_data)
        for serial_data in serials_data:
            VokalatnamaSerial.objects.create(sale=sale, **serial_data)
        return sale
    

    def update(self, instance, validated_data):
        serials_data = validated_data.pop('bailbond_serials', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if serials_data is not None:
            instance.serials.all().delete()
            for serial_data in serials_data:
                VokalatnamaSerial.objects.create(sale=instance, **serial_data)

        return instance