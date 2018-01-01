/*
Kyle Finter
finter179
5/4/16
lab13 creates two circles and allows user to set the radius for one of them, then shows area, circumference, and diameter
*/

#include <iostream>

using namespace std;

class Circle{
    private:
        double radius;
    public:
        double PI=3.14159;
        Circle(){
            this->radius=0.0;
        };
        Circle(double r){
            this->radius=r;
        };
        void setRadius(double r);
        double getRadius(){
            return this->radius;
        };
        double getArea(){
            return PI*radius*radius;
        };
        double getDiameter(){
            return radius*2;
        };
        double getCircumference(){
            return 2*PI*radius;
        };
};

void Circle::setRadius(double r){
    if (r>=0.0)
        radius=r;
    else
        cout<<"Error! You must supply a non-negative value."<<endl;
};

int main(){
    double userRadius=0.0;
    Circle c1;
    cout<<"Here is the first circle's data after using the default constructor for creating the circle:"<<endl;
    cout<<"Radius: "<<c1.getRadius()<<endl;
    cout<<"Diameter: "<<c1.getDiameter()<<endl;
    cout<<"Area: "<<c1.getArea()<<endl;
    cout<<"Circumference: "<<c1.getCircumference()<<endl<<endl;

    cout<<"What value do you want to set the radius to? ";
    cin>>userRadius;
    c1.setRadius(userRadius);

    cout<<endl<<"Here is the first circle's data after setting the radius to "<<userRadius<<":"<<endl;
    cout<<"Radius: "<<c1.getRadius()<<endl;
    cout<<"Diameter: "<<c1.getDiameter()<<endl;
    cout<<"Area: "<<c1.getArea()<<endl;
    cout<<"Circumference: "<<c1.getCircumference()<<endl<<endl;

    Circle c2(12.5);
    cout<<endl<<"Here is the second circle's data:"<<endl;
    cout<<"Radius: "<<c2.getRadius()<<endl;
    cout<<"Diameter: "<<c2.getDiameter()<<endl;
    cout<<"Area: "<<c2.getArea()<<endl;
    cout<<"Circumference: "<<c2.getCircumference()<<endl<<endl;

    return 0;
}
