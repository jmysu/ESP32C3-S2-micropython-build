# ESP32C3-micropython-build
building ESP32C3 micropython notes
<br><br>


Clone esp-idf repository; For ESP32-C3/S2 need V4.3.1+
  $ git clone -b v4.4 --recursive https://github.com/espressif/esp-idf.git


After you've cloned and checked out the IDF to the correct version, run the install.sh script:
  $ cd esp-idf
  $ ./install.sh       # (or install.bat on Windows)
  $ source export.sh   # (or export.bat on Windows)
The install.sh step only needs to be done once. 
You will need to source export.sh for every new session. (For environment variables)
(Or $export ESP_IDF=~/esp_idf $source export.sh)

Clone MicroPython repository...
  $ git clone https://www.github.com/micropython/micropython<br>
  $ cd micropython/<br>
  $ make -C mpy-cross/<br>

  $ cd ports/esp32<br>
  $ make submodules
  $ make BOARD=GENERIC_C3 -j4<br>
  $cd build-GENERIC_C3
  <br><br>
  This will produce a combined firmware.bin image in the build-GENERIC/ subdirectory (this firmware image is made up of: bootloader.bin, partitions.bin and micropython.bin).


Project build complete. To flash, run this command:
$ esptool.py --chip esp32c3 --port /dev/cu.wchusbserialfd130 --baud 460800 write_flash -z 0x0 firmware.bin

---

To use the PyDOS, follows instructions on https://github.com/RetiredWizard/PyDOS <br>
(use MPRemote to copy PyDOS contents into micropython local folder)<br>
<img src="pic/PyDOS-micropython.png"/>
<br>
See http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html for a quick reference, and http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html for a tutorial.
<br>
<br>
## Reference <br>
[General information about the ESP32 port]https://docs.micropython.org/en/latest/esp32/general.html<br>
[How to build MicroPython for esp32-C3]https://www.jarutex.com/index.php/2022/01/04/9217/<br>
[Awesome resources collections] https://github.com/mcauser/awesome-micropython<br>
[PyDOS] https://github.com/RetiredWizard/PyDOS

