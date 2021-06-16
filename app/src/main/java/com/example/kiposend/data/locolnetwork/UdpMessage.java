package com.example.kiposend.data.locolnetwork;

import java.util.Objects;

public class UdpMessage<E> {
    E message;
    int age=0;
    int maxAge;

    public UdpMessage(E message, int maxAge){
        this.message=message;
        this.maxAge=maxAge;
    }

    public E GetMessage(){
        return message;
    }
    public void IncreaseAge(){
        age++;
    }
    public void Revalidate(){
        age=0;
    }
    public boolean IsValid(){
        return age<=maxAge;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UdpMessage<?> that = (UdpMessage<?>) o;
        return message.equals(that.message);
    }

    @Override
    public int hashCode() {
        return Objects.hash(message);
    }
}
