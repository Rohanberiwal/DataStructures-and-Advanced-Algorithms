import java.util.*;

class Main {
    public static void insertionSort(int array[], int size) {
        for (int pos = 1; pos < size; pos++) {
            int nextpos = pos;
            while (nextpos > 0 && array[nextpos] < array[nextpos - 1]) {
                int temp = array[nextpos];
                array[nextpos] = array[nextpos - 1];
                array[nextpos - 1] = temp;
                nextpos = nextpos - 1;
            }
        }
        for (int i = 0; i < size; i++) {
            System.out.print(" " + array[i]);
        }
    }

    public static void main(String[] args) {
        System.out.println("Enter the array size: ");
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int array[] = new int[size];
        System.out.println("Enter array elements: ");
        for (int i = 0; i < size; i++) {
            array[i] = sc.nextInt();
        }

        insertionSort(array, size);
    }
}
