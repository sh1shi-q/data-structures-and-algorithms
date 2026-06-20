#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* array;
    int capacity;
    int size;
} DynamicArray;

void initArray(DynamicArray* arr, int initialCapacity) {
    if (initialCapacity <= 0) {
        printf("Initial capacity must be greater than 0.\n");
        exit(1);
    }
    arr->capacity = initialCapacity;
    arr->size = 0;
    arr->array = (int*)malloc(initialCapacity * sizeof(int));
}

void freeArray(DynamicArray* arr) {
    free(arr->array);
    arr->array = NULL;
    arr->capacity = 0;
    arr->size = 0;
}

int getSize(DynamicArray* arr) {
    return arr->size;
}

int getCapacity(DynamicArray* arr) {
    return arr->capacity;
}

int get(DynamicArray* arr, int index) {
    if (index < 0 || index >= arr->size) {
        printf("Index out of bounds.\n");
        exit(1);
    }
    return arr->array[index];
}

int set(DynamicArray* arr, int index, int value) {
    if (index < 0 || index >= arr->size) {
        printf("Index out of bounds.\n");
        exit(1);
    }
    arr->array[index] = value;
}

void resize(DynamicArray* arr) {
    arr->capacity *= 2;
    int* newArray = (int*)malloc(arr->capacity * sizeof(int));
    for (int i = 0; i < arr->size; i++) {
        newArray[i] = arr->array[i];
    }
    free(arr->array);
    arr->array = newArray;
}

void add(DynamicArray* arr, int value) {
    if (arr->size == arr->capacity) {
        resize(arr);
    }
    arr->array[arr->size++] = value;
}

void removeAt(DynamicArray* arr, int index) {
    if (index < 0 || index >= arr->size) {
        printf("Index out of bounds.\n");
        exit(1);
    }
    for (int i = index; i < arr->size - 1; i++) {
        arr->array[i] = arr->array[i + 1];
    }
    arr->size--;
}

int pop(DynamicArray* arr) {
    if (arr->size == 0) {
        printf("Array is empty.\n");
        exit(1);
    }
    return arr->array[--arr->size];
}

int main() {
    DynamicArray arr;
    initArray(&arr, 2);

    add(&arr, 10);
    add(&arr, 20);
    add(&arr, 30);

    for (int i = 0; i < getSize(&arr); i++) {
        printf("%d ", get(&arr, i));
    }
    printf("\n");

    pop(&arr);
    for (int i = 0; i < getSize(&arr); i++) {
        printf("%d ", get(&arr, i));
    }
    printf("\n");

    removeAt(&arr, 0);
    for (int i = 0; i < getSize(&arr); i++) {
        printf("%d ", get(&arr, i));                    
    }
    printf("\n");

    freeArray(&arr);
    return 0;
}