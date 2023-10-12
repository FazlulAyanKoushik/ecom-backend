"""Serializer for Product model."""

from rest_framework import serializers

from product.models import Product


class ProductBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "uid",
            "slug",
            "name",
            "brand",
            "category",
            "manufacturer",
            "buying_price",
            "mrp",
            "discounted",
            "discounted_price",
            "stock",
            "is_published",
            "is_salesable",
            "image",
            "rating",
        )
        read_only_fields = (
            "id",
            "uid",
            "slug",
        )


class ProductListSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + ()
        read_only_fields = ProductBaseSerializer.Meta.read_only_fields + ()

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class ProductDetailSerializer(ProductBaseSerializer):
    class Meta(ProductBaseSerializer.Meta):
        fields = ProductBaseSerializer.Meta.fields + (
            "entry_by",
            "updated_by",
            "created_at",
            "updated_at",
        )
        read_only_fields = ProductBaseSerializer.Meta.read_only_fields + (
            "created_at",
            "updated_at",
            "entry_by",
            "updated_by",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        validated_data["updated_by_id"] = user.id
        return super().update(instance, validated_data)
