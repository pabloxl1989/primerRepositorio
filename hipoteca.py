saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108


while saldo > 0:
    pago_extra = mes > 60 and mes <=108
    if pago_extra:
        saldo = saldo * (1 + tasa/12) - pago_mensual - adelanto
        total_pagado = total_pagado + pago_mensual + adelanto
        mes += 1
        print(mes, round(total_pagado, 2), round(saldo, 2))

    if not pago_extra:
        if pago_mensual <= saldo:
            saldo = saldo * (1 + tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
            mes += 1
            print(mes, round(total_pagado, 2), round(saldo, 2))

        else:
            pago_mensual = saldo * (1 + tasa/12)
            saldo = saldo * (1 + tasa/12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
            mes += 1
            print(mes, round(total_pagado, 2), round(saldo, 2))





print('Total pagado', round(total_pagado, 2), mes)