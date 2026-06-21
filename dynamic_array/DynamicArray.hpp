#ifndef DYNAMIC_ARRAY_HPP
#define DYNAMIC_ARRAY_HPP

class DynamicArray {
private:
    int* array;
    int capacity;
    int size;
    void resize();

public:
    DynamicArray(int startingCapacity);

    ~DynamicArray();

    void add(int value);
    void removeAt(int index);
    int getSize();
    int getCapacity();
    int get(int index);
    void set(int index, int value);
};

#endif