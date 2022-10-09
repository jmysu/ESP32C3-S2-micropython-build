# ESP32C3-micropython-build
building ESP32C3 micropython notes
<br><br>


Clone esp-idf repository; For ESP32-C3/S2 need V4.3.1+<br>
> _git clone -b v4.4 --recursive https://github.com/espressif/esp-idf.git_ <br>
<br>

After you've cloned and checked out the IDF to the correct version, run the install.sh script:<br>
> _cd esp-idf_ <br>
> _./install.sh_       # (or install.bat on Windows)<br>
> _source export.sh_   # (or export.bat on Windows)<br>

The install.sh step only needs to be done once. <br>
You will need to source export.sh for every new session. (For environment variables)<br>
(Or $export ESP_IDF=~/esp_idf $source export.sh)<br>
<br>

Clone MicroPython repository...<br>
> _git clone https://www.github.com/micropython/micropython_ <br>
> _cd micropython/_ <br>
> _make -C mpy-cross/_ <br>
> _cd ports/esp32_<br>
> _make submodules_<br>
> _make BOARD=GENERIC_C3 -j4_<br>
> _cd build-GENERIC_C3_<br>

<br>
This will produce a combined firmware.bin image in the build-GENERIC_C3/ subdirectory<br>
(this firmware image is made up of: bootloader.bin, partitions.bin and micropython.bin).<br>

Project build complete. To flash, run this command:<br>
> _esptool.py --chip esp32c3 --port /dev/cu.wchusbserialfd130 --baud 460800 write_flash -z 0x0 firmware.bin_<br>
> 
<img src="pic/ESP32micropython.png"/><br>Thonny connectted to micropython w/ PyDOS.
<br>
  
<img src="pic/micropythonHwInfo.png"/><br>micropython display hwInfo.
<br>

<br>
---
<br>
See http://docs.micropython.org/en/latest/esp32/quickref.html for a quick reference,<br>
and http://docs.micropython.org/en/latest/esp32/tutorial/intro.html for a tutorial.
<br>
<br>

## Reference <br>

[General information about the ESP32 port] https://docs.micropython.org/en/latest/esp32/general.html<br>
[How to build MicroPython for esp32-C3] https://www.jarutex.com/index.php/2022/01/04/9217/<br>
[Awesome resources collections] https://github.com/mcauser/awesome-micropython<br>
[PyDOS] https://github.com/RetiredWizard/PyDOS

