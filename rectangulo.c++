#include <iostream>

class rectangulo {

private:
    double base;
    double altura;

public:
    rectangulo (double b, double a) : base(b), altura(a) {}

    double area() {
        return base * altura;
    }

    double perimetro() {
        int suma= base + altura;
        int Perimetro= 2 * suma;
        return Perimetro;
    }

    void cambiar_base (double b) {
        base= b;
    }

    void cambiar_altura(double a) {
        altura=a;
    }

    void imprimir () {
        std::cout << "base: " << base << std::endl;
        std::cout << "altura: " << altura << std::endl;
        std::cout << "area: " << area() << std::endl;
        std::cout << "Perimetro: " << perimetro() << std::endl;
    }

};

int main() {
    double base= 6;
    double altura= 8;

    rectangulo Rectangulo(base, altura);
    Rectangulo.imprimir();

    return 0;

}