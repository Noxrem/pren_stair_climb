################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/croutine.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/event_groups.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/list.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/queue.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/stream_buffer.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/tasks.c \
C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/timers.c 

OBJS += \
./McuLib/FreeRTOS/Source/croutine.o \
./McuLib/FreeRTOS/Source/event_groups.o \
./McuLib/FreeRTOS/Source/list.o \
./McuLib/FreeRTOS/Source/queue.o \
./McuLib/FreeRTOS/Source/stream_buffer.o \
./McuLib/FreeRTOS/Source/tasks.o \
./McuLib/FreeRTOS/Source/timers.o 

C_DEPS += \
./McuLib/FreeRTOS/Source/croutine.d \
./McuLib/FreeRTOS/Source/event_groups.d \
./McuLib/FreeRTOS/Source/list.d \
./McuLib/FreeRTOS/Source/queue.d \
./McuLib/FreeRTOS/Source/stream_buffer.d \
./McuLib/FreeRTOS/Source/tasks.d \
./McuLib/FreeRTOS/Source/timers.d 


# Each subdirectory must supply rules for building sources it contributes
McuLib/FreeRTOS/Source/croutine.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/croutine.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/event_groups.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/event_groups.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/list.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/list.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/queue.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/queue.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/stream_buffer.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/stream_buffer.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/tasks.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/tasks.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

McuLib/FreeRTOS/Source/timers.o: C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/McuLib/FreeRTOS/Source/timers.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__REDLIB__ -DCPU_MK22FN512VDC12 -DCPU_MK22FN512VDC12_cm4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=0 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\board" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\source" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\drivers" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\device" -I"C:\Users\Noxrem\Documents\GitHub\pren_stair_climb\TinyK22_McuLib\PrenTeam_TinyK22_McuLib\CMSIS" -I../../McuLib -I../../McuLib/config -I../../McuLib/config/fonts -I../../McuLib/fonts -I../../McuLib/src -I../../McuLib/FreeRTOS/Source/include -I../../McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F -I../../McuLib/SEGGER_RTT -I../../McuLib/SEGGER_Sysview -I../../McuLib/TraceRecorder -I../../McuLib/TraceRecorder/config -I../../McuLib/TraceRecorder/include -I../../McuLib/TraceRecorder/streamports/Jlink_RTT/include -I../../McuLib/HD44780 -I../../McuLib/FatFS -I../../McuLib/FatFS/source -include"C:/Users/Noxrem/Documents/GitHub/pren_stair_climb/TinyK22_McuLib/PrenTeam_TinyK22_McuLib/source/IncludeMcuLibConfig.h" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="../$(@D)/"=. -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


