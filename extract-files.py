#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/sm8350',
    'hardware/xiaomi',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/sm8350-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/etc/camera/pureShot_parameter.xml', 'vendor/etc/camera/pureView_parameter.xml'): blob_fixup()
        .regex_replace(r'=(\d+)>', r'="\1">'),
    'vendor/lib/hw/audio.primary.redwood.so': blob_fixup()
        .replace_needed('/vendor/lib/liba2dpoffload.so', '/odm/lib/liba2dpoffload.so')
        .replace_needed('/vendor/lib/libssrec.so', '/odm/lib/libssrec.so')
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib/libaudioroute_ext.so': blob_fixup()
        .replace_needed('libaudioroute.so', 'libaudioroute-v34.so'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .binary_regex_replace(b'\x73\x74\x5F\x6C\x69\x63\x65\x6E\x73\x65\x2E\x6C\x69\x63', b'\x63\x61\x6D\x65\x72\x61\x5F\x63\x6E\x66\x2E\x74\x78\x74')
        .add_needed('libprocessgroup_shim.so'),
    'vendor/lib64/hw/camera.xiaomi.so': blob_fixup()
        .sig_replace('29 07 00 94', '1F 20 03 D5'),
    'vendor/lib64/hw/com.qti.chi.override.so' : blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    ('vendor/lib64/libmialgo_rfs.so'): blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
        .clear_symbol_version('remote_register_buf_attr')
        .clear_symbol_version('remote_session_control'),
    ('vendor/lib64/libalAILDC.so', 'vendor/lib64/libalLDC.so', 'vendor/lib64/libalhLDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/libarcsoft_hdrplus_hvx_stub.so': blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    'vendor/lib64/libsensor_cal_v2.so': blob_fixup()
        .add_needed('libjsoncpp_shim.so'),
}  # fmt: skip


module = ExtractUtilsModule(
    'redwood',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8350-common', module.vendor
    )
    utils.run()
