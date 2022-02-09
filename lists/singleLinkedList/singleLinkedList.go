package singleLinkedList

import (
	"ds/lists"
	"ds/utils"
	"fmt"
	"strings"
)

//
func assertListImplementation() {
	var _ lists.List = (*List)(nil)
}

// using gods's struct method using struct to
// initialize singlelinkedlist, not interface
type List struct {
	first, last *element
	size        int
}

// element is used inside
type element struct {
	value interface{}
	next  *element
}

// New instantiates a new list and adds the passed values, if any, to the list
func New(values ...interface{}) *List {
	list := &List{}
	if len(values) > 0 {
		list.Add(values...)
	}
	return list
}

// Add appends a value (one or more) at the end of the list (same as Append())
func (list *List) Add(values ...interface{}) {
	for _, value := range values {
		newElement := &element{value: value}
		if list.size == 0 {
			list.first = newElement
			list.last = newElement
		} else {
			list.last.next = newElement
			list.last = newElement
		}
		list.size++
	}
}

// Append appends a value (one or more) at the end of the list (same as Add())
func (list *List) Append(values ...interface{}) {
	list.Add(values...)
}

// Prepend prepends a values (or more)
// in reverse to keep passed order i.e. ["c","d"] -> Prepend(["a","b"]) -> ["a","b","c",d"]
func (list *List) Prepend(values ...interface{}) {
	// for v := len(values) - 1; v >= 0; v-- {
	// 	newElement := &element{value: values[v], next}
	// }
}

// Get returns the element at index.
// Second return parameter is true if index is within bounds of the array and array is not empty, otherwise false.
func (list *List) Get(index int) (interface{}, bool) {
	// out of index
	if !(list.withinRange(index)) {
		return nil, false
	}

	curr := list.first
	for i := 0; i < index; i++ {
		curr = curr.next
	}
	return curr.value, true
}

// Remove removes the element at the given index from the list.
func (list *List) Remove(index int) {
}

// Contains checks if values (one or more) are present in the set.
// All values have to be present in the set for the method to return true.
// Performance time complexity of n^2.
// Returns true if no arguments are passed at all, i.e. set is always super-set of empty set.
func (list *List) Contains(values ...interface{}) bool {
	return true
}

// Values returns all elements in the list.
func (list *List) Values() []interface{} {
	values := make([]interface{}, list.size)
	for e, element := 0, list.first; element != nil; e, element = e+1, element.next {
		values[e] = element.value
	}
	return values
}

// IndexOf returns index of provided element
func (list *List) IndexOf(value interface{}) int {
	return 0
}

// Empty returns true if list does not contain any elements.
func (list *List) Empty() bool {
	return list.size == 0
}

// Size returns number of elements within the list.
func (list *List) Size() int {
	return list.size
}

// Clear removes all elements from the list.
func (list *List) Clear() {
}

// Sort sort values (in-place) using.
func (list *List) Sort(comparator utils.Comparator) {

}

// Swap swaps values of two elements at the given indices.
func (list *List) Swap(i, j int) {}

// Insert inserts values at specified index position shifting the value at that position (if any) and any subsequent elements to the right.
// Does not do anything if position is negative or bigger than list's size
// Note: position equal to list's size is valid, i.e. append.
func (list *List) Insert(index int, values ...interface{}) {
	if !list.withinRange(index) {
		if index == list.size {
			list.Add(values...) // append
		}
		return
	}
	list.size += len(values)

	var beforeE *element
	foundE := list.first
	for i := 0; i < index; i++ {
		beforeE, foundE = foundE, foundE.next
	}

	if foundE == list.first {
		// insert before first/head node
		oldNextE := list.first
		for i, v := range values {
			newE := &element{value: v}
			if i == 0 {
				list.first = newE
			} else {
				beforeE.next = newE
			}
			beforeE = newE
		}
		beforeE.next = oldNextE
	} else {
		oldNextE := beforeE.next
		for _, v := range values {
			newE := &element{value: v}
			beforeE.next = newE
			beforeE = newE
		}
		beforeE.next = oldNextE
	}
}

// Set value at specified index
// Does not do anything if position is negative or bigger than list's size
// Note: position equal to list's size is valid, i.e. append.
func (list *List) Set(index int, value interface{}) {
	// out of index
	if !(list.withinRange(index)) {
		if index == list.size {
			list.Add(value)
		}
		return
	}
	curr := list.first
	for i := 0; i < index; i++ {
		curr = curr.next
	}
	curr.value = value
}

// String returns a string representation of container
func (list *List) String() string {
	str := "singleLinkedList: "
	values := []string{}
	for e := list.first; e != nil; e = e.next {
		values = append(values, fmt.Sprintf("%v", e.value))
	}
	str += strings.Join(values, " -> ")
	return str
}

// Check that the index is within bounds of the list
func (list *List) withinRange(index int) bool {
	return index >= 0 && index < list.size
}
