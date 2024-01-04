import java.util.*;

class Main {
    public static void selectionSort(int array[], int size, int startpos) {
        if (startpos < size - 1) {
            int minpos = findMinPosition(array, startpos, size - 1);
            int temp = array[startpos];
            array[startpos] = array[minpos];
            array[minpos] = temp;

            // Recursively sort the rest of the array
            selectionSort(array, size, startpos + 1);
        }
    }

    public static int findMinPosition(int array[], int start, int end) {
        int minpos = start;
        for (int i = start + 1; i <= end; i++) {
            if (array[i] < array[minpos]) {
                minpos = i;
            }
        }
        return minpos;
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

        selectionSort(array, size, 0);

        // Print sorted array
        System.out.println("Sorted array:");
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
    }
}
