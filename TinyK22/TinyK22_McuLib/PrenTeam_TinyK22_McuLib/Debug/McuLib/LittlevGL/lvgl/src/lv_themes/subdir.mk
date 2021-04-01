################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_alien.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_default.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_material.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_mono.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_nemo.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_night.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_templ.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_zen.c 

OBJS += \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_alien.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_default.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_material.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_mono.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_nemo.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_night.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_templ.o \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_zen.o 

C_DEPS += \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_alien.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_default.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_material.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_mono.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_nemo.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_night.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_templ.d \
./McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_zen.d 


# Each subdirectory must supply rules for building sources it contributes
McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_alien.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_alien.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_default.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_default.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_material.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_material.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_mono.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_mono.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_nemo.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_nemo.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_night.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_night.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_templ.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_templ.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_zen.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_themes/lv_theme_zen.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


