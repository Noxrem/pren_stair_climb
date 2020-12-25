################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_fmt_txt.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_12.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_16.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_22.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_28.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_unscii_8.c 

OBJS += \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_fmt_txt.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_12.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_16.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_22.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_28.o \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_unscii_8.o 

C_DEPS += \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_fmt_txt.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_12.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_16.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_22.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_28.d \
./McuLib/LittlevGL/lvgl/src/lv_font/lv_font_unscii_8.d 


# Each subdirectory must supply rules for building sources it contributes
McuLib/LittlevGL/lvgl/src/lv_font/lv_font.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_fmt_txt.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_fmt_txt.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_12.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_12.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_16.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_16.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_22.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_22.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_28.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_roboto_28.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_font/lv_font_unscii_8.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_font/lv_font_unscii_8.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


