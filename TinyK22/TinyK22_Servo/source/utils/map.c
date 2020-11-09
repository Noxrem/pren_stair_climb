/**
 *--------------------------------------------------------------------\n
 *          HSLU T&A Hochschule Luzern Technik+Architektur            \n
 *--------------------------------------------------------------------\n
 *
 * \brief         Mapping a numeric range into another
 * \file
 * \author        Pascal Brülhart
 * \date          07.11.2020
 *
 *--------------------------------------------------------------------
 */

#include <stdint.h>
#include "map.h"

/**
 * Maps (transforms) a value in a given range to another range
 *
 * Note: Since division in C is truncating a "divPrecision"-Factor is introduced.
 * So the out_max needs to be about the factor divPrecision smaller than INT32_MAX.
 * Otherwise there will be an overflow!
 *
 * @param[in] value
 *    Integer value to map from one range to another
 * @param[in] in_min
 *    Min. possible value of the range of "value"
 * @param[in] in_max
 *    Max. possible value of the range of "value"
 * @param[in] out_min
 * 	  Min. possible value of the range the output value should be
 * @param[in] out_max
 *    Max. possible value of the range the output value should be
 * @return
 *    The "value" mapped to the output range
 */
int32_t mapRangeToAnother(int32_t value, int32_t in_min, int32_t in_max, int32_t out_min, int32_t out_max)
{
	int32_t divPrecision = 100;
	int32_t slope = (divPrecision * (out_max - out_min)) / (in_max - in_min);
	return out_min + (slope * (value - in_min) / divPrecision);
}


