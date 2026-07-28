class Pedido:

    def calcular_pedido(
        self,
        primer_plato: str,
        costo_primer_plato: float,
        bebida: str,
        costo_bebida: float,
        segundo_plato: str = None,
        costo_segundo_plato: float = None,
        postre: str = None,
        costo_postre: float = None,
    ):

        if segundo_plato is None and postre is None:
            total = costo_primer_plato + costo_bebida
            print(
                f"El costo de {primer_plato} y {bebida} es = ${total}"
            )

        elif segundo_plato is not None and postre is None:
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print(
                f"El costo de {primer_plato} + {segundo_plato} "
                f"+ {bebida} es = ${total}"
            )

        else:
            total = (
                costo_primer_plato
                + costo_segundo_plato
                + costo_postre
                + costo_bebida
            )
            print(
                f"El costo de {primer_plato} + {segundo_plato} "
                f"+ {bebida} + {postre} es = ${total}"
            )