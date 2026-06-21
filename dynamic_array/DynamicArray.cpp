#include "DynamicArray.hpp"
#include <iostream>

DynamicArray::DynamicArray(int startingCapacity) {
    if (startingCapacity <= 0) {
        std::cerr << "Initial capacity must be greater than 0." << std::endl;
        exit(1);
    }
    this->capacity = startingCapacity;
    this->size = 0;
    this->array = new int[this->capacity];
}

DynamicArray::~DynamicArray() {
    delete[] this->array;
}

void DynamicArray::add(int value) {
    if (this->size >= this-> capacity) {
        this->resize();
    }
    this->array[this->size++] = value;
}

void DynamicArray::removeAt(int index) {
    if ( index < 0 || index >= this->size ) {
        std::cerr << "Index out of bounds." << std::endl;
        exit(1);
    }
    for (int i = index; i < this->size - 1; i++) {
        this->array[i] = this->array[i + 1];
    }
    this->size--;
}

int DynamicArray::getSize() {
    return this->size;
}

int DynamicArray::getCapacity() {
    return this->capacity;
}

int DynamicArray::get(int index) {
    if (index < 0 || index >= this->size) {
        std::cerr << "Index out of bounds." << std::endl;
        exit(1);
    }
    return this->array[index];
}

void DynamicArray::set(int index, int value) {
    if (index < 0 || index >= this->size) {
        std::cerr << "Index out of bounds." << std::endl;
        exit(1);
    }
    this->array[index] = value;
}

void DynamicArray::resize() {
    this->capacity *= 2;
    int* newArray = new int[this->capacity];
    for (int i = 0; i < this->size; i++) {
        newArray[i] = this->array[i];
    }
    delete[] this->array;
    this->array = newArray;
}

int main() {
    DynamicArray arr(2);

    std::cout << "adding 1, 2" << std::endl;
    arr.add(1);
    arr.add(2);

    std::cout << "size: " << arr.getSize() << std::endl;
    std::cout << "capacity: " << arr.getCapacity() << std::endl;

    arr.add(3);
    std::cout << "added 3, size: " << arr.getSize() << std::endl;
    std::cout << "capacity: " << arr.getCapacity() << std::endl;

    std::cout << "removing at index 1" << std::endl;
    arr.removeAt(1);
    std::cout << "size: " << arr.getSize() << std::endl;
    std::cout << "element at index 1: " << arr.get(1) << std::endl; 

    for (int i = 0; i < arr.getSize(); i++) {
        std::cout << "index " << i << ": " << arr.get(i) << std::endl;
    }

    return 0;
};