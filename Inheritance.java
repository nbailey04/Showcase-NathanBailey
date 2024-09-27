//The following should go in a file called "Employee.java"

public class Employee extends Person implements Compensable {
    private String employeeID;
    private Department department;
    protected double salary;
    private Role role;
    private BonusStrategy bonusStrategy;

    public Employee(String name, int age, String address, String employeeID, Department department, double salary, Role role, BonusStrategy bonusStrategy) {
        super(name, age, address);
        this.employeeID = employeeID;
        this.department = department;
        this.salary = salary;
        this.role = role;
        this.bonusStrategy = bonusStrategy;
    }

    public double getSalary() {
        return salary;
    }

    public Department getDepartment() {
        return department;
    }

    public Role getRole() {
        return role;
    }

    public double calculateCompensation() {
        return salary + bonusStrategy.calculateBonus(this);
    }

    public void displayEmployeeInfo() {
        displayPersonInfo();
        System.out.println("Role: " + role);
        System.out.println("Department: " + department);
        System.out.printf("Salary: $%,.2f%n", salary);
        System.out.printf("Total Compensation: $%,.2f%n", calculateCompensation());
    }
}



//The following should go in a file called "Manager.java"

public class Manager extends Employee {
    private int teamSize;
    private double bonus;

    public Manager(String name, int age, String address, String employeeID, Department department, double salary, int teamSize, double bonus) {
        super(name, age, address, employeeID, department, salary, Role.MANAGER, new PerformanceBonusStrategy());
        this.teamSize = teamSize;
        this.bonus = bonus;
    }

    public double getBonus() {
        return bonus;
    }

    @Override
    public void displayEmployeeInfo() {
        super.displayEmployeeInfo();
        System.out.println("Team Size: " + teamSize);
    }
}


//The following should go in a file called "Person.java"

public class Person {
    String name;
    int age;
    String address;

    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public void displayPersonInfo() {
        System.out.println("Person Information:");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Address: " + address);
    }


}


//The following should go in a file called "BonusStrategy.java"

// BonusStrategy Interface
public interface BonusStrategy {
    double calculateBonus(Employee employee);
}

// PerformanceBonusStrategy for Managers
class PerformanceBonusStrategy implements BonusStrategy {
    @Override
    public double calculateBonus(Employee employee) {
        if (employee instanceof Manager) {
            Manager manager = (Manager) employee;
            return manager.getSalary() * 0.10 + manager.getBonus(); // 10% of salary + performance bonus
        }
        return 0;
    }
}

// ProjectBonusStrategy for Engineers
class ProjectBonusStrategy implements BonusStrategy {
    @Override
    public double calculateBonus(Employee employee) {
        return employee.getSalary() * 0.05; // Engineers get 5% of salary as project bonus
    }
}

// FixedBonusStrategy for other employees
class FixedBonusStrategy implements BonusStrategy {
    @Override
    public double calculateBonus(Employee employee) {
        return 1000; // Fixed bonus amount
    }
}




//The following should go in a file called "Compensable.java"

public interface Compensable {
    double calculateAnnualSalary();
}



//The following should go in a file called "Printable.java"

public interface Printable {
    void displayEmployeeInfo();
}


//The following should go in a file called "ReportGenerator.java"

package SoftwareEngineering.Lab1;

import java.util.List;

public class ReportGenerator {
    public void generateDepartmentReport(List<Employee> employees, Department department) {
        System.out.println("Report for Department: " + department);
        for (Employee employee : employees) {
            if (employee.getDepartment() == department) {
                employee.displayEmployeeInfo();
                System.out.println("-------------------------------");
            }
        }
    }

    public void generateRoleReport(List<Employee> employees, Role role) {
        System.out.println("Report for Role: " + role);
        for (Employee employee : employees) {
            if (employee.getRole() == role) {
                employee.displayEmployeeInfo();
                System.out.println("-------------------------------");
            }
        }
    }
}


//The following should go in a file called "Role.java"

public enum Role {
    MANAGER,
    ENGINEER,
    HR_REPRESENTATIVE,
    SALES_PERSON
}


//The following should go in a file called "main.java"

import java.util.Arrays;
import java.util.List;

public class main {
    public static void main(String[] args) {
        Employee engineer = new Employee("John Doe", 30, "123 Maple Street", "E12345", Department.ENGINEERING, 85000.00, Role.ENGINEER, new ProjectBonusStrategy());
        Manager manager = new Manager("Alice Johnson", 40, "789 Birch Lane", "M67890", Department.IT, 95000.00, 5, 10000.00);
        Employee hrRep = new Employee("Emma Davis", 35, "456 Oak Avenue", "H11234", Department.HR, 60000.00, Role.HR_REPRESENTATIVE, new FixedBonusStrategy());

        // List of employees
        List<Employee> employees = Arrays.asList(engineer, manager, hrRep);

        // Generate reports
        ReportGenerator reportGenerator = new ReportGenerator();
        reportGenerator.generateDepartmentReport(employees, Department.IT);
        reportGenerator.generateRoleReport(employees, Role.ENGINEER);
    }
}



