################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include startup/subdir.mk
-include source/utils/subdir.mk
-include source/sound/subdir.mk
-include source/servo/subdir.mk
-include source/io/subdir.mk
-include source/i2c/subdir.mk
-include source/drive/subdir.mk
-include source/com/subdir.mk
-include source/adc/subdir.mk
-include source/subdir.mk
-include drivers/subdir.mk
-include device/subdir.mk
-include board/subdir.mk
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
all: pren_stari_climb.axf

# Tool invocations
pren_stari_climb.axf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: MCU Linker'
	arm-none-eabi-gcc -nostdlib -Xlinker -Map="pren_stari_climb.map" -Xlinker --gc-sections -Xlinker -print-memory-usage -Xlinker --sort-section=alignment -Xlinker --cref -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -T "Pren_tinyk22_Debug.ld" -o "pren_stari_climb.axf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '
	$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(EXECUTABLES)$(OBJS)$(C_DEPS) pren_stari_climb.axf
	-@echo ' '

post-build:
	-@echo 'Performing post-build steps'
	-arm-none-eabi-size "pren_stari_climb.axf" ; arm-none-eabi-objdump -S pren_stari_climb.axf > pren_stari_climb.lst ; #arm-none-eabi-objcopy -O ihex pren_stari_climb.axf pren_stari_climb.hex ; # arm-none-eabi-objcopy -v -O binary "pren_stari_climb.axf" "pren_stari_climb.bin" ; # checksum -p MK22FN512xxx12 -d "pren_stari_climb.bin"
	-@echo ' '

.PHONY: all clean dependents post-build

-include ../makefile.targets
