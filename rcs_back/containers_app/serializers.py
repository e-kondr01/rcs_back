from rest_framework import serializers

from .models import Container, Building


class FillContainerSerializer(serializers.ModelSerializer):
    """ Сериализатор для заполнения контейнера """
    class Meta:
        model = Container
        fields = ["id", "is_full"]

    def validate_is_full(self, value):
        """ Этот сериализатор используется только для того,
        чтобы заполнить контейнер """
        if not value:
            msg = "is_full can be only true for this view"
            raise serializers.ValidationError(msg)
        return value


class ActivateContainerSerializer(serializers.ModelSerializer):
    """ Сериализатор для активации контейнера """
    class Meta:
        model = Container
        fields = ["id", "status"]

    def validate_status(self, value):
        """ Этот сериализатор используется только для того,
        чтобы активировать контейнер """
        if value != 2:
            msg = "status can be only 2 for this view"
            raise serializers.ValidationError(msg)
        return value


class ContainerSerializer(serializers.ModelSerializer):
    """ Сериализатор контейнера"""
    building = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Container
        fields = [
            "id",
            "building",
            "building_part",
            "floor",
            "location",
            "capacity",
            "is_full",
            "status",
            "is_public",
            "created_at",
            "email",
            "phone",
            "cur_fill_time",
            "cur_takeout_wait_time",
            "avg_fill_time",
            "avg_takeout_wait_time"
        ]


class ChangeContainerSerializer(serializers.ModelSerializer):
    """ Сериализатор контейнера с цифрой для статуса
    и id у здания"""
    building = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all()
    )

    class Meta:
        model = Container
        fields = [
            "id",
            "building",
            "building_part",
            "floor",
            "location",
            "capacity",
            "is_full",
            "status",
            "is_public",
            "created_at",
            "email",
            "phone",
            "cur_fill_time",
            "cur_takeout_wait_time",
            "avg_fill_time",
            "avg_takeout_wait_time"
        ]


class BuildingSerializer(serializers.ModelSerializer):
    """Сериализатор здания"""
    class Meta:
        model = Building
        fields = [
            "id",
            "address"
        ]


class ContainerStickerSerializer(serializers.ModelSerializer):
    """Сериализатор стикера контейнера"""
    class Meta:
        model = Container
        fields = [
            "id",
            "sticker"
        ]


class ContainerPublicAddSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления контейнера рандомами"""
    building = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all()
    )

    class Meta:
        model = Container
        fields = [
            "id",
            "email",
            "phone",
            "building",
            "building_part",
            "floor",
            "location",
            "capacity"
        ]
        extra_kwargs = {
            "email": {"required": True},
            "phone": {"required": True}
        }
