# general
make_debug = False
make_task = ""

targets = ["ios", "macos", "android"]
targets = ["android"]

# pdfium
pdfium_git_commit = "46ff50212421a1959bc4adbe476ffeac2c6aa593"
# ^ ref: https://pdfium.googlesource.com/pdfium/+/refs/heads/chromium/4408

# macos
configurations_macos = ["release"]
targets_macos = [
    {"target_os": "macos", "target_cpu": "x64", "pdfium_os": "mac"},
    {"target_os": "macos", "target_cpu": "arm64", "pdfium_os": "mac"},
]

# ios
configurations_ios = ["release"]
targets_ios = [
    {"target_os": "ios", "target_cpu": "arm", "pdfium_os": "ios"},
    {"target_os": "ios", "target_cpu": "arm64", "pdfium_os": "ios"},
    {"target_os": "ios", "target_cpu": "x64", "pdfium_os": "ios"},
]
sdks_ios = [
    "iphoneos",
    "iphonesimulator",
]

# android
configurations_android = ["release"]
targets_android = [
    {
        "target_os": "android",
        "target_cpu": "arm",
        "pdfium_os": "android",
        "android_cpu": "armeabi-v7a",
    },
    {
        "target_os": "android",
        "target_cpu": "x86",
        "pdfium_os": "android",
        "android_cpu": "x86",
    },
    {
        "target_os": "android",
        "target_cpu": "arm64",
        "pdfium_os": "android",
        "android_cpu": "arm64-v8a",
    },
    {
        "target_os": "android",
        "target_cpu": "x64",
        "pdfium_os": "android",
        "android_cpu": "x86_64",
    },
]

# wasm
configurations_wasm = ["release"]
targets_wasm = [
    {"target_os": "linux", "target_cpu": "x64", "pdfium_os": "linux"},
]
