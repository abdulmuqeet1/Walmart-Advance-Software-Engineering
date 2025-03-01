import java.util.Arrays;
import java.util.NoSuchElementException;

public class ExponentialHeap {
    private double exponent;
    private int currentSize;
    private int[] heapData;

    public ExponentialHeap(double exponent, int capacity) {
        this.currentSize = 0;
        heapData = new int[capacity + 1];
        this.exponent = exponent;
        Arrays.fill(heapData, -1);
    }

    private int getParentIndex(int index) {
        int power = (int) Math.pow(2, exponent);
        return (index - 1) / power;
    }

    public boolean isHeapFull() {
        return currentSize == heapData.length;
    }

    public void addValue(int value) {
        if (isHeapFull()) {
            throw new NoSuchElementException("Heap is full.");
        } else {
            heapData[currentSize++] = value;
            restoreHeapOrderUp(currentSize - 1);
        }
    }

    private void restoreHeapOrderUp(int index) {
        int temp = heapData[index];
        while (index > 0 && temp > heapData[getParentIndex(index)]) {
            heapData[index] = heapData[getParentIndex(index)];
            index = getParentIndex(index);
        }
        heapData[index] = temp;
    }

    public int removeMaxValue() {
        int maxVal = heapData[0];
        heapData[0] = heapData[currentSize - 1];
        heapData[currentSize - 1] = -1;
        currentSize--;

        int index = 0;
        while (index < currentSize - 1) {
            restoreHeapOrderUp(index);
            index++;
        }

        return maxVal;
    }

    public void displayHeap() {
        for (int i = 0; i < currentSize; i++) {
            System.out.print(heapData[i]);
            if (i < currentSize - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ExponentialHeap heap = new ExponentialHeap(
            2, // exponent
            100 // capacity
        );
        heap.addValue(2);
        heap.addValue(7);
        heap.addValue(41);
        heap.addValue(16);

        heap.displayHeap();

        int maxVal = heap.removeMaxValue();
        System.out.println("Max Value: " + maxVal);

        heap.displayHeap();
    }
}
