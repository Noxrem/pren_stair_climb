################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_arc.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_basic.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_img.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_label.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_line.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_rect.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_triangle.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_cache.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_decoder.c 

OBJS += \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_arc.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_basic.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_img.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_label.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_line.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_rect.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_triangle.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_cache.o \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_decoder.o 

C_DEPS += \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_arc.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_basic.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_img.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_label.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_line.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_rect.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_triangle.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_cache.d \
./McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_decoder.d 


# Each subdirectory must supply rules for building sources it contributes
McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_arc.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_arc.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_basic.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_basic.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_img.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_img.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_label.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_label.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_line.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_line.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_rect.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_rect.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_triangle.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_draw_triangle.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_cache.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_cache.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_decoder.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/LittlevGL/lvgl/src/lv_draw/lv_img_decoder.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


