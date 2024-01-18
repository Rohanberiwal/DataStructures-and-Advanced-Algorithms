#include <iostream>
#include <complex>
#include <valarray>

const double PI = 3.141592653589793238460;

typedef std::complex<double> Complex;
typedef std::valarray<Complex> ComplexArray;

void fft(ComplexArray& x) {
    const size_t N = x.size();
    if (N <= 1) return;

    ComplexArray even = x[std::slice(0, N/2, 2)];
    ComplexArray odd = x[std::slice(1, N/2, 2)];

    fft(even);
    fft(odd);

    for (size_t k = 0; k < N/2; ++k) {
        Complex t = std::polar(1.0, -2.0 * PI * k / N) * odd[k];
        x[k] = even[k] + t;
        x[k + N/2] = even[k] - t;
    }
}

int main() {
    // Example usage
    ComplexArray data = {1.0, 2.0, 3.0, 4.0};
    
    // Perform FFT
    fft(data);

    // Display FFT results
    std::cout << "FFT result:" << std::endl;
    for (size_t i = 0; i < data.size(); ++i) {
        std::cout << "X[" << i << "] = " << data[i] << std::endl;
    }

    return 0;
}
