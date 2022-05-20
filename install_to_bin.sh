#!/bin/bash
echo "[i] Bây giờ chúng tôi sẽ cài đặt Raven-Storm vào đường dẫn bin của bạn..."
if [ -d "/usr/share/Raven-Storm" ] ; then
    echo "[i] Đã tìm thấy phiên bản cũ của Raven-Storm, đang tiếp tục cập nhật..."
    echo "[i] Sao lưu phiên bản cũ."
    if [ -d "/usr/share/Raven-Storm/Backup" ] ; then
        sudo mv /usr/share/Raven-Storm/Backup ./Backup
    else
        mkdir ./Backup
    fi
    name="./Backup/Raven-Storm"
    if [ -d $name ] ; then
        i=0
        while [ -d "$name.bak$i" ] ; do
            let i++
        done
            name="$name.bak$i"
    fi
    sudo mv /usr/share/Raven-Storm $name
    mv ./Backup ./Raven-Storm/
    sudo cp -ar ./Raven-Storm /usr/share/
    echo "[i] cài đặt thành công."
    echo "[i] Làm cho Raven-Storm có thể thực thi..."
    sudo mv /usr/share/Raven-Storm/main.py /usr/share/Raven-Storm/rst
    sudo chmod +x /usr/share/Raven-Storm/rst
    sudo ln -s /usr/share/Raven-Storm/rst /usr/bin/rst || echo "[i] Liên kết dường như đã tồn tại."
else
    sudo cp -ar ./Raven-Storm /usr/share/
    echo "[i] cài đặt thành công."
    echo "[i] Làm cho Raven-Storm có thể thực thi..."
    sudo mv /usr/share/Raven-Storm/main.py /usr/share/Raven-Storm/rst
    sudo chmod +x /usr/share/Raven-Storm/rst
    sudo ln -s /usr/share/Raven-Storm/rst /usr/bin/rst || echo "[i] Liên kết dường như đã tồn tại."
fi

echo "[i] Chương trình được dịch bởi Đậu Đậu 5.0"
echo "[i] Bạn có thể xóa thư mục Raven-Storm ngay bây giờ."
echo "----------------------------------------"
echo "[i] Chạy 'sudo rst' để bắt đầu Raven-Storm."
echo "----------------------------------------"
exit 0
