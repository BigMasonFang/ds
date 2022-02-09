package arraylist

import (
	"errors"
	"fmt"
)

const DEFAULT_CAPACITY int = 10

type List interface {
	Size() int
	Find(val interface{}) int
	Contains(val interface{}) bool

	Get(index int) (interface{}, error)

	Set(index int, newVal interface{}) error

	Insert(index int, val interface{}) error
	Append(index int, val interface{})

	Remove(index int) error
	Remove2(index int) error
	Pop(index int) interface{} // same as remove but return
	RemoveElement(val interface{}) error
	RemoveElement2(val interface{}) error

	Clear()

	String() string
}

type Iterator interface {
	HasNext() bool
	Next() (interface{}, error)
	Remove()
}

type Iterable interface {
	Iterator() Iterator
}

type arrayListIterator struct {
	list    *ArrayList
	current int
}

type ArrayList struct {
	datastore []interface{}
	theSize   int
}

func New() *ArrayList {
	list := new(ArrayList)
	list.Clear()
	return list
}

func (list *ArrayList) resize(size int) {
	// create a new sized list
	newDS := make([]interface{}, 0, size)
	// copy old data to new one
	copy(newDS, list.datastore)
	// assignment
	list.datastore = newDS
}

func (list *ArrayList) ensureCapacity() {
	// automatic enlarge
	if list.Size() == cap(list.datastore) {
		list.resize(list.Size() * 2)
		// automatic shrink
		// to avoid time complexity shock, using mild approach
	} else if list.Size() == (cap(list.datastore)/4) && list.Size()/2 != 0 {
		list.resize(list.Size() / 2)
	}
}

func (list *ArrayList) Size() int {
	return list.theSize
}

func (list *ArrayList) Find(val interface{}) int {
	for i := 0; i < list.Size(); i++ {
		if list.datastore[i] == val {
			return i
		}
	}
	return -1
}

func (list *ArrayList) Contains(val interface{}) bool {
	return list.Find(val) >= 0
}

func (list *ArrayList) Get(index int) (interface{}, error) {
	if index < 0 || index >= list.Size() {
		return nil, errors.New("index out of range")
	}
	return list.datastore[index], nil
}

func (list *ArrayList) Set(index int, newVal interface{}) error {
	if index < 0 || index >= list.Size() {
		return errors.New("index out of range")
	}
	list.datastore[index] = newVal
	return nil
}

func (list *ArrayList) Insert(index int, val interface{}) error {
	if index < 0 || index > list.Size() {
		return errors.New("index out of range")
	}
	list.ensureCapacity()
	list.datastore = list.datastore[:list.Size()+1] // length add 1

	for i := list.Size(); i > index; i-- {
		list.datastore[i] = list.datastore[i-1]
	}
	list.datastore[index] = val
	list.theSize++

	return nil
}

func (list *ArrayList) Append(val interface{}) {
	// list.ensureCapacity() ? need?
	// no append will enlarge the cap automatically
	list.datastore = append(list.datastore, val)
	list.theSize++
}

func (list *ArrayList) Remove(index int) error {
	// smart way
	if index < 0 || index >= list.Size() {
		return errors.New("index out of range")
	}
	list.datastore = append(list.datastore[:index], list.datastore[index+1:]...)
	list.theSize--
	// shrink
	list.ensureCapacity()
	return nil
}

func (list *ArrayList) Remove2(index int) error {
	// traditional way
	if index < 0 || index >= list.Size() {
		return errors.New("index out of range")
	}
	for i := index; i < list.Size()-1; i++ {
		list.datastore[i] = list.datastore[i+1]
	}
	// cut size
	list.theSize--
	// adjust array
	list.datastore = list.datastore[:list.Size()]
	// shrink
	list.ensureCapacity()
	return nil
}

func (list *ArrayList) Pop(index int) interface{} {
	if index < 0 || index >= list.Size() {
		return errors.New("index out of range")
	}
	result := list.datastore[index]
	for i := index; i < list.Size()-1; i++ {
		list.datastore[i] = list.datastore[i+1]
	}
	// cut size
	list.theSize--
	// adjust array
	list.datastore = list.datastore[:list.Size()]
	// shrink
	list.ensureCapacity()
	return result
}

func (list *ArrayList) RemoveElement(val interface{}) error {
	// smart way
	index := list.Find(val)
	if index == -1 {
		return errors.New("val do not exist")
	}
	list.Remove(index)
	// shrink
	list.ensureCapacity()
	return nil
}

func (list *ArrayList) RemoveElement2(val interface{}) error {
	// traditional way
	index := -1
	for i := 0; i < list.Size(); i++ {
		if list.datastore[i] == val {
			index = i
			break
		}
	}
	if index == -1 {
		return errors.New("val do not exist")
	}
	for i := index; i < list.Size()-1; i++ {
		list.datastore[i] = list.datastore[i+1]
	}
	// cut size
	list.theSize--
	// adjust array
	list.datastore = list.datastore[:list.Size()]
	// shrink
	list.ensureCapacity()
	return nil
}

func (list *ArrayList) Clear() {
	list.datastore = make([]interface{}, 0, DEFAULT_CAPACITY)
	list.theSize = 0
}

func (list *ArrayList) String() string {
	return fmt.Sprint(list.datastore)
}

// funcs for arrayListIterator
func (list *ArrayList) Iterator() Iterator {
	iterator := new(arrayListIterator)
	iterator.current = 0
	iterator.list = list
	return iterator
}

func (it *arrayListIterator) HasNext() bool {
	return it.current < it.list.Size()
}

func (it *arrayListIterator) Next() (interface{}, error) {
	if !it.HasNext() {
		return nil, errors.New("no such element")
	}
	v, err := it.list.Get(it.current)
	it.current++
	return v, err
}

func (it *arrayListIterator) Remove() {
	it.current--
	it.list.Remove(it.current)
}
