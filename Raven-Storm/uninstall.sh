#!/bin/bash
echo "[i] Bây giờ chúng tôi sẽ gỡ cài đặt Raven-Storm..."
echo "[i] Thao tác này sẽ xóa tất cả các bản sao lưu."
sudo rm -i /usr/bin/rst
sudo rm -rf -i /usr/share/Raven-Storm

echo "[i] Đã gỡ cài đặt thành công Raven-Storm."
exit 0
