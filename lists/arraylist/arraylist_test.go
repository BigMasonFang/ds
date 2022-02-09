package arraylist

import (
	"fmt"
	"reflect"
	"testing"
)

func TestSize(t *testing.T) {
	list := New()
	if list.Size() != 0 {
		t.Errorf("new arraylist's size should not be zero")
		t.Fail()
	}
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	if list.Size() != 4 {
		t.Errorf("arraylist#Size() failed. error list size:%d, expected size:4.", list.Size())
		t.Fail()
	}
}

func TestAppend(t *testing.T) {
	list := New()
	var list_validate []interface{}
	for i := 0; i < 4; i++ {
		list.Append(i)
		if list.Size() != i+1 {
			t.Errorf("arraylist's Size() is %d, expected: %d", list.Size(), i+1)
			t.Fail()
		}
		list_validate = append(list_validate, i)
		if reflect.DeepEqual(list.datastore, list_validate) != true {
			t.Errorf("arraylist's datastore is %s, expected: %v", list.String(), list_validate)
			t.Fail()
		}
	}
}

func TestFind(t *testing.T) {
	list := New()
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	idx_1 := list.Find("i")
	if idx_1 != 2 {
		t.Errorf("arrayList#Find() failed. wrong idx: %d, expected: %d", idx_1, 2)
	}
	idx_2 := list.Find("k")
	if idx_2 != -1 {
		t.Errorf("arrayList#Find() failed. wrong idx: %d, expected: %d", idx_2, -1)
	}
}

func TestGet(t *testing.T) {
	list := New()
	list.Append("h")
	list.Append("w")
	list.Append(1)
	list.Append(4)
	val, ok := list.Get(0)
	if ok != nil || val != "h" {
		t.Errorf("arrayList#Get() failed. wrong val: %s, expected: %s or wrong status: %v, expected : %v",
			val, "h", ok, nil)
	}
	val_wrong, ok_wrong := list.Get(5)
	if ok_wrong.Error() != "index out of range" || val_wrong != nil {
		t.Errorf("arrayList#Get() failed. wrong val: %s, expected: %v or wrong status: %v, expected : %s",
			val_wrong, nil, ok_wrong, ok_wrong.Error())
	}
}

func TestSet(t *testing.T) {
	list := New()
	list.Append("h")
	list.Append("w")
	list.Set(0, 1)
	val, ok := list.Get(0)
	if val != 1 || ok != nil {
		t.Errorf("arrayList#Set() failed. wrong val: %v, expected: %d", val, 1)
	}
}

func TestInsert(t *testing.T) {
	list := New()
	list.Append("h")
	list.Append("w")
	list.Append(1)
	list.Append(4)
	list.Insert(4, "T")
	val, ok := list.Get(4)
	fmt.Println(list)
	if val != "T" || ok != nil {
		t.Errorf("arraylist#Insert() failed. val %s is not get right", val)
		t.Fail()
	}
}

func TestRemove(t *testing.T) {
	list := New()
	test_element := "h"
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	// remove
	list.Remove(0)
	list_validate := New()
	list_validate.Append("w")
	list_validate.Append("i")
	list_validate.Append("j")
	if list.Contains(test_element) {
		t.Errorf("arraylist#Remove() failed. element %s not removed", test_element)
		t.Fail()
	}
	if reflect.DeepEqual(list, list_validate) != true {
		t.Errorf("arraylist#Remove() failed. list not equal)")
		t.Fail()
	}
}

func TestRemove2(t *testing.T) {
	list := New()
	test_element := "h"
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	// remove
	list.Remove2(0)
	list_validate := New()
	list_validate.Append("w")
	list_validate.Append("i")
	list_validate.Append("j")
	if list.Contains(test_element) {
		t.Errorf("arraylist#Remove() failed. element %s not removed", test_element)
		t.Fail()
	}
	if reflect.DeepEqual(list, list_validate) != true {
		t.Errorf("arraylist#Remove() failed. list not equal)")
		t.Fail()
	}
}
func TestRemoveElment(t *testing.T) {
	// delete
	list := New()
	test_element := "w"
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	list.RemoveElement(test_element)
	if list.Contains(test_element) {
		t.Errorf("arraylist#Remove() failed. element %s not deleted", test_element)
		t.Fail()
	}
	list_validate_2 := New()
	list_validate_2.Append("h")
	list_validate_2.Append("i")
	list_validate_2.Append("j")
	if reflect.DeepEqual(list, list_validate_2) != true {
		t.Errorf("arraylist#Delete() failed. list not equal)")
		t.Fail()
	}
}

func TestRemoveElment2(t *testing.T) {
	// delete
	list := New()
	test_element := "w"
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	list.RemoveElement2(test_element)
	if list.Contains(test_element) {
		t.Errorf("arraylist#Remove() failed. element %s not deleted", test_element)
		t.Fail()
	}
	list_validate_2 := New()
	list_validate_2.Append("h")
	list_validate_2.Append("i")
	list_validate_2.Append("j")
	if reflect.DeepEqual(list, list_validate_2) != true {
		t.Errorf("arraylist#Delete() failed. list not equal)")
		t.Fail()
	}
}
func TestPop(t *testing.T) {
	// pop
	list := New()
	test_element := "i"
	list.Append("h")
	list.Append("w")
	list.Append("i")
	list.Append("j")
	to_pop_element := list.datastore[2]
	pop_element := list.Pop(2)
	if list.Contains(pop_element) {
		t.Errorf("arraylist#Pop() failed. element %s not deleted", test_element)
		t.Fail()
	}
	if pop_element != to_pop_element {
		t.Errorf("arraylist#Pop() failed. pop elements not equal")
		t.Fail()
	}
	list_validate_3 := New()
	list_validate_3.Append("h")
	list_validate_3.Append("w")
	list_validate_3.Append("j")
	if reflect.DeepEqual(list, list_validate_3) != true {
		t.Errorf("arraylist#Delete() failed. list not equal)")
		t.Fail()
	}
}

func TestAutomaticEnlarge(t *testing.T) {
	list := New()
	for i := 0; i < 11; i++ {
		list.Append(i)
	}
	if cap(list.datastore) != 20 {
		t.Errorf("arraylist ensureCapacity() failed. cap is %d, expected %d", cap(list.datastore), 20)
		t.Fail()
	}
}

func TestAutomaticShrink(t *testing.T) {
	list := New()
	for i := 0; i < 11; i++ {
		list.Append(i)
	}
	list.Remove(10)
	if cap(list.datastore) != 5 {
		t.Errorf("arraylist ensureCapacity() failed. cap is %d, expected %d", cap(list.datastore), 5)
		t.Fail()
	}
}
