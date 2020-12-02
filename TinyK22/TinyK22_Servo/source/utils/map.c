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
 * @param[in] x
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
int32_t mapRangeToAnother(int32_t x, int32_t in_min, int32_t in_max, int32_t out_min, int32_t out_max)
{
	if ((in_max - in_min) > (out_max - out_min))
	{
		return (x - in_min) * (out_max - out_min + 1) / (in_max - in_min + 1)
				+ out_min;
	}
	else
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}


