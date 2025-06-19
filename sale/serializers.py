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
            'id', 'receipt_no', 'sale_type', 'sales_date', 'advocate_name', 'advocateId',
            'building_name', 'address', 'customer_phone', 'customer_name',
            'customer_address','price', 'total_count', 'total_amount', 'serials'
        ]

    def create(self, validated_data):
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
        fields = ['id', 'receipt_no', 'sales_date','building_name','remarks', 'total_count', 'total_amount','bailbond_serials']

    def create(self, validated_data):
        serials_data = validated_data.pop('bailbond_serials')
        print(serials_data)
        sale = Bailbond.objects.create(**validated_data)
        for serial_data in serials_data:
            BailbondSerial.objects.create(sale=sale, **serial_data)
        return sale
    

    def update(self, instance, validated_data):
        serials_data = validated_data.pop('bailbond_serials', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if serials_data is not None:
            instance.serials.all().delete()
            for serial_data in serials_data:
                BailbondSerial.objects.create(sale=instance, **serial_data)

        return instance
    





class FormSerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSerial
        fields = ['id', 'from_serial', 'to_serial', 'total']



class FormSaleSerializer(serializers.ModelSerializer):
    form_serials = FormSerialSerializer(many=True)

    class Meta:
        model = FormSale
        fields = ['id', 'receipt_no', 'sales_date', 'building_name', 'form_name',
                  'remarks', 'form_serials', 'total_count', 'price', 'total_amount']

    def create(self, validated_data):
        form_serials_data = validated_data.pop('form_serials')
        sale = FormSale.objects.create(**validated_data)
        for serial in form_serials_data:
            FormSerial.objects.create(form_sale=sale, **serial)
        return sale
    

    def update(self, instance, validated_data):
        serials_data = validated_data.pop('form_serials', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if serials_data is not None:
            instance.serials.all().delete()
            for serial_data in serials_data:
                FormSerial.objects.create(sale=instance, **serial_data)

        return instance
    






class AssociateRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociateRegistration
        fields = '__all__'

        


class AssociateRenewalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociateRenewal
        fields = '__all__'






class HallRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallRentCollection
        fields = '__all__'






class HouseRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentCollection
        fields = '__all__'




class EntryFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryFee
        fields = '__all__'




class MonthlyFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyFee
        fields = '__all__'



class BarFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarAssociationFee
        fields = '__all__'



class AdvocateAllFeeSerializer(serializers.ModelSerializer):
    rentcollection_set = HouseRentSerializer(many=True, required=False)
    entryfee_set = EntryFeeSerializer(many=True, required=False)
    monthlyfee_set = MonthlyFeeSerializer(many=True, required=False)
    barassociationfee_set = BarFeeSerializer(many=True, required=False)

    class Meta:
        model = AdvocateAllFee
        fields = ['id', 'advocate_id', 'collection_date', 'receipt_no',
                  'rentcollection_set', 'entryfee_set', 'monthlyfee_set', 'barassociationfee_set']

    def create(self, validated_data):
        rent_data = validated_data.pop('rentcollection_set', [])
        entry_data = validated_data.pop('entryfee_set', [])
        monthly_data = validated_data.pop('monthlyfee_set', [])
        bar_data = validated_data.pop('barassociationfee_set', [])

        print(rent_data,entry_data,monthly_data,bar_data)

        advocate_fee = AdvocateAllFee.objects.create(**validated_data)

        for rent in rent_data:
            RentCollection.objects.create(advocate_all_fee=advocate_fee, **rent)

        for entry in entry_data:
            EntryFee.objects.create(advocate_all_fee=advocate_fee, **entry)

        for monthly in monthly_data:
            MonthlyFee.objects.create(advocate_all_fee=advocate_fee, **monthly)

        for bar in bar_data:
            BarAssociationFee.objects.create(advocate_all_fee=advocate_fee, **bar)

        return advocate_fee
    


    def update(self, instance, validated_data):
        rent_data = validated_data.pop('rentcollection_set', [])
        entry_data = validated_data.pop('entryfee_set', [])
        monthly_data = validated_data.pop('monthlyfee_set', [])
        bar_data = validated_data.pop('barassociationfee_set', [])

        # Update base AdvocateAllFee fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Optionally: delete old and recreate new nested items
        instance.rentcollection_set.all().delete()
        for rent in rent_data:
            RentCollection.objects.create(advocate_all_fee=instance, **rent)

        instance.entryfee_set.all().delete()
        for entry in entry_data:
            EntryFee.objects.create(advocate_all_fee=instance, **entry)

        instance.monthlyfee_set.all().delete()
        for monthly in monthly_data:
            MonthlyFee.objects.create(advocate_all_fee=instance, **monthly)

        instance.barassociationfee_set.all().delete()
        for bar in bar_data:
            BarAssociationFee.objects.create(advocate_all_fee=instance, **bar)

        return instance






class AdvocateChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateChange
        fields = '__all__'
        read_only_fields = ['receipt_no']




class FundCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundCollection
        fields = '__all__'





class BillCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillCollection
        fields = '__all__'



class BankInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInterest
        fields = '__all__'