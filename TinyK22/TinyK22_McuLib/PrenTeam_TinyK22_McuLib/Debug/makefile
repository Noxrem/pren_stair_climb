################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include startup/subdir.mk
-include source/subdir.mk
-include drivers/subdir.mk
-include device/subdir.mk
-include board/subdir.mk
-include McuLib/src/subdir.mk
-include McuLib/fonts/subdir.mk
-include McuLib/SEGGER_Sysview/subdir.mk
-include McuLib/SEGGER_RTT/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_themes/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_objx/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_misc/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_hal/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_font/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_draw/subdir.mk
-include McuLib/LittlevGL/lvgl/src/lv_core/subdir.mk
-include McuLib/LittlevGL/lvgl/porting/subdir.mk
-include McuLib/FreeRTOS/Source/portable/MemMang/subdir.mk
-include McuLib/FreeRTOS/Source/portable/GCC/ARM_CM4F/subdir.mk
-include McuLib/FreeRTOS/Source/portable/Common/subdir.mk
-include McuLib/FreeRTOS/Source/subdir.mk
-include McuLib/FreeRTOS/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: PrenTeam_TinyK22_McuLib.axf

# Tool invocations
PrenTeam_TinyK22_McuLib.axf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: MCU Linker'
	arm-none-eabi-gcc -nostdlib -Xlinker -Map="PrenTeam_TinyK22_McuLib.map" -Xlinker --gc-sections -Xlinker -print-memory-usage -Xlinker --sort-section=alignment -Xlinker --cref -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -T PrenTeam_TinyK22_McuLib_Debug.ld -o "PrenTeam_TinyK22_McuLib.axf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '
	$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(EXECUTABLES)$(OBJS)$(C_DEPS) PrenTeam_TinyK22_McuLib.axf
	-@echo ' '

post-build:
	-@echo 'Performing post-build steps'
	-arm-none-eabi-size "PrenTeam_TinyK22_McuLib.axf"; # arm-none-eabi-objcopy -v -O binary "PrenTeam_TinyK22_McuLib.axf" "PrenTeam_TinyK22_McuLib.bin" ; # checksum -p MK22FN512xxx12 -d "PrenTeam_TinyK22_McuLib.bin";
	-@echo ' '

.PHONY: all clean dependents post-build

-include ../makefile.targets
