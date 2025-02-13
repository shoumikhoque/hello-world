def change_memoization(amount, coins) :
    if amount == 0:
        return 1
    for i in range(len(coins)):
        if coins[i]>amount:
            coins=coins[:i+1]
            break

    dp=[[0]*(len(coins)) for _ in range(amount+1)]
    def calc(amount, pos):
        if amount==0:
            return 1
        if amount<0 or pos>=len(coins):
            return 0
        if dp[amount][pos]==0:
            if coins[pos]<=amount:
                 dp[amount][pos]=calc(amount - coins[pos], pos)
            dp[amount][pos] +=calc(amount,pos+1)
        return dp[amount][pos]
        if dp[amount][pos]!=0:
            return dp[amount][pos]
        for i in range(pos, len(coins)):
            if coins[i] == amount:
                dp[amount][pos] += 1
            elif coins[i] < amount:
                dp[amount][pos] += calc(amount - coins[i], i)
        return dp[amount][pos]

    return calc(amount, 0)
def change_tabulation(amount, coins) :
    if amount == 0:
        return 1
    dp = [[0] * len(coins) for x in range(amount+1)]
    for i in range(len(coins)):
        dp[0][i]=1
    for target in range(1,amount+1):
        for j in range(len(coins)):
            if coins[j]==target:
                dp[target][j]+=1
            elif coins[j]<target:
                dp[target][j]+=(dp[target-coins[j]][j]+dp[target][coins[j]])
    return sum(dp[amount])

# 5
# [5,2,1]


if __name__ == '__main__':
    amount = 4000
    coins = [200,217,234,251,268,285,302,319,336,353,370,387,404,421,438,455,472,489,506,523,540,557,574,591,608,625,642,659,676,693,710,727,744,761,778,795,812,829,846,863,880,897,914,931,948,965,982,999,1016,1033,1050,1067,1084,1101,1118,1135,1152,1169,1186,1203,1220,1237,1254,1271,1288,1305,1322,1339,1356,1373,1390,1407,1424,1441,1458,1475,1492,1509,1526,1543,1560,1577,1594,1611,1628,1645,1662,1679,1696,1713,1730,1747,1764,1781,1798,1815,1832,1849,1866,1883,1900,1917,1934,1951,1968,1985,2002,2019,2036,2053,2070,2087,2104,2121,2138,2155,2172,2189,2206,2223,2240,2257,2274,2291,2308,2325,2342,2359,2376,2393,2410,2427,2444,2461,2478,2495,2512,2529,2546,2563,2580,2597,2614,2631,2648,2665,2682,2699,2716,2733,2750,2767,2784,2801,2818,2835,2852,2869,2886,2903,2920,2937,2954,2971,2988,3005,3022,3039,3056,3073,3090,3107,3124,3141,3158,3175,3192,3209,3226,3243,3260,3277,3294,3311,3328,3345,3362,3379,3396,3413,3430,3447,3464,3481,3498,3515,3532,3549,3566,3583,3600,3617,3634,3651,3668,3685,3702,3719,3736,3753,3770,3787,3804,3821,3838,3855,3872,3889,3906,3923,3940,3957,3974,3991,4008,4025,4042,4059,4076,4093,4110,4127,4144,4161,4178,4195,4212,4229,4246,4263,4280,4297,4314,4331,4348,4365,4382,4399,4416,4433,4450,4467,4484,4501,4518,4535,4552,4569,4586,4603,4620,4637,4654,4671,4688,4705,4722,4739,4756,4773,4790,4807,4824,4841,4858,4875,4892,4909,4926,4943,4960,4977,4994]
    # amount=5
    # coins=[5,2,1]
    print(change_tabulation(amount,coins))