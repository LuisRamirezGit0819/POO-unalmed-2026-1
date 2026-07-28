class ArticuloCientifico:

    def __init__(
        self,
        titulo: str,
        autor: str,
        palabras_claves: list[str] = None,
        publicacion: str = None,
        anno: int = None,
        resumen: str = None,
    ):
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves: list[str] = [None, None, None]
        self.publicacion = None
        self.anno = None
        self.resumen = None

        if palabras_claves is not None:
            self.palabras_claves = palabras_claves
            self.publicacion = publicacion
            self.anno = anno

        if resumen is not None:
            self.resumen = resumen

    def imprimir(self):
        print(f"Titulo del articulo = {self.titulo}")
        print(f"Autor del articulo = {self.autor}")
        print("Palabras clave = ")
        for palabra in self.palabras_claves:
            if palabra is not None:
                print(f"  {palabra}")
        print(f"Publicacion = {self.publicacion}")
        print(f"Anno = {self.anno}")
        print(f"Resumen = {self.resumen}")