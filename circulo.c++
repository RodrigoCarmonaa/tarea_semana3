#include <iostream>

class Circulo {
private:
    double radio;

public:
    Circulo(double r) : radio(r) {}

    double area() {
        return 3.14 * (radio * radio);
    }

    double perimetro() {
        return 2 * 3.14 * radio;
    }

    void cambiar_radio(double r) {
        radio = r;
    }

    void imprimir() {
        std::cout << "Radio: " << radio << std::endl;
        std::cout << "Area: " << area() << std::endl;
        std::cout << "Perimetro: " << perimetro() << std::endl;
    }
};

int main() {
    double radioUsuario;
    std::cout << "Ingrese el radio del círculo: ";
    std::cin >> radioUsuario;

    Circulo circulo(radioUsuario);
    circulo.imprimir();

    return 0;
}