#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8350-common
$(call inherit-product, device/xiaomi/sm8350-common/common.mk)

# Overlays
DEVICE_PACKAGE_OVERLAYS += \
    $(LOCAL_PATH)/overlay

# Overlays-RRO
PRODUCT_PACKAGES += \
    RedwoodCNSettingsProviderOverlay \
    RedwoodCNWifiOverlay \
    RedwoodGLSettingsProviderOverlay \
    RedwoodGLWifiOverlay \
    RedwoodINSettingsProviderOverlay \
    RedwoodINWifiOverlay

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Call the proprietary setup
$(call inherit-product, vendor/xiaomi/redwood/redwood-vendor.mk)
