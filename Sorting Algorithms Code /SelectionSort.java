import java.util.*;

class Main {
    public static void selectionSort(int array[], int size) {
        for (int startpos = 0; startpos < size; startpos++) {
            int minpos = startpos;
            for (int i = startpos + 1; i < size; i++) {
                if (array[i] < array[minpos]) {
                    minpos = i;
                }
            }
            int temp = array[startpos];
            array[startpos] = array[minpos];
            array[minpos] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the array size");
        int size = sc.nextInt();
        int array[] = new int[size];
        for (int i = 0; i < size; i++) {
            System.out.println("Enter array element " + i);
            array[i] = sc.nextInt();
        }

        selectionSort(array, size);

        // Print sorted array
        System.out.println("Sorted array:");
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
