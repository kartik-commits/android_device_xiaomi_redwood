#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/redwood

# Inherit from sm8350-common
include device/xiaomi/sm8350-common/BoardConfigCommon.mk

# Kernel
TARGET_KERNEL_CONFIG += vendor/redwood_QGKI.config

# Include proprietary files
include vendor/xiaomi/redwood/BoardConfigVendor.mk
