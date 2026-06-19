public class IntArray {
    private int[] array; 
    private int capacity;
    private int size;

    public IntArray(int capacity) {
        if ( capacity <= 0) {
            throw new IllegalArgumentException("capacity must be greater than 0");
        }
        this.capacity = capacity;
        this.size = 0;
        this.array = new int[capacity];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void add(int value) {
        if (size == capacity) {
            resize();
        }
        array[size] = value;
        size++;
    }

    private void resize() {
        capacity *= 2;
        int[] newArray = new int[capacity];
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        array = newArray;
    }

    public int get(int index) {
        if ( index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index: " + index + ", size: " + size);
        }
        return array[index];
    }

    public void set(int index, int value) {
        if ( index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index: " + index + ", size: " + size);
        }
        array[index] = value;
    }

    public void remove(int index) {
        if ( index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index: " + index + ", size: " + size);
        }
        for (int i = index; i < size - 1; i++) {
            array[i] = array[i + 1];
        }
        size--;
    }

    public int pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Array is empty");
        }
        int value = array[size - 1];
        size--;
        return value;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < size; i++){
            sb.append(array[i]);
            if (i < size - 1) {
                sb.append(" ,");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        IntArray intArray = new IntArray(2);

        intArray.add(1);
        intArray.add(2);
        System.out.println(intArray); 

        intArray.add(3);
        System.out.println(intArray); 

        System.out.println(intArray.get(1)); 

        intArray.set(1, 20);
        System.out.println(intArray); 

        intArray.remove(0);
        System.out.println(intArray);
         
        System.out.println(intArray.pop()); 
        System.out.println(intArray); 
    }

} 


