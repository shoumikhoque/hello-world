if __name__ == '__main__':
    sal=100000
    mon=13
    inc_rate=0.15
    inv_rate=1
    yr_inv_grw=0.10
    total_inv=0
    for i in range(12):
        yr_sal = sal * mon
        yr_inv = yr_sal * inv_rate
        total_inv+=yr_inv
        total_ret=(total_inv)*(yr_inv_grw)
        total_inv+=total_ret
        print(f"{i}->{sal:.2f},{yr_inv:.2f},{total_inv:.2f}")
        sal*=(1+inc_rate)
