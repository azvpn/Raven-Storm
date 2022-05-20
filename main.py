#!/usr/bin/python3

# 2020
# Bộ công cụ Raven-Storm được lập trình và phát triển bởi Taguar258.
# Bộ công cụ Raven-Storm được xuất bản theo Giấy phép MIT.
# Bộ công cụ Raven-Storm dựa trên CLIF-Framework.
# CLIF-Framework được lập trình và phát triển bởi Taguar258.
# CLIF-Framework được xuất bản theo Giấy phép MIT.

# Tập lệnh này là một lối tắt cho tất cả những ai không muốn cài đặt Raven-Storm vào đường dẫn bin.

from importlib import import_module
from sys import path

path.insert(1, "./Raven-Storm/")
main = import_module("Raven-Storm.main")

main.run()
