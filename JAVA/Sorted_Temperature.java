// Using Linear Search Algorithm

public class Sorted_Temperature {
    
    String city;
    int temperature;
    private static final int citiesLength = 10;
    
    private Sorted_Temperature(String city, int temperature) {
        this.city = city;
        this.temperature = temperature;
    }
    
    public static void main(String[] args) {
        
        Sorted_Temperature[] temp = new Sorted_Temperature[citiesLength];
        
        System.out.println("Average July Temperatures by City");
        
        addCites(temp);
        sortTemp(temp);
        
        for (Sorted_Temperature sorted_Temp : temp) {
            if (sorted_Temp != null) {
                System.out.println(sorted_Temp.city + ": " + sorted_Temp.temperature);
            }
        }
    }
    
    static void addCites(Sorted_Temperature[] temp) {
        temp[0] = new Sorted_Temperature("New Delhi", 45);
        temp[1] = new Sorted_Temperature("Bangalore", 37);
        temp[2] = new Sorted_Temperature("Faridabad", 41);
        temp[3] = new Sorted_Temperature("Guwahati", 34);
        temp[4] = new Sorted_Temperature("Thiruvanthapuram", 37);
        temp[5] = new Sorted_Temperature("Pune", 36);
        temp[6] = new Sorted_Temperature("Ladakh", 30);
        temp[7] = new Sorted_Temperature("Chandigarh", 39);
        temp[8] = new Sorted_Temperature("Jaipur", 46);
        temp[9] = new Sorted_Temperature("Noida", 40);
    }
    
    static void sortTemp(Sorted_Temperature[] temp) {
        
        for (int i = 0; i < citiesLength; i++) {
            int firstIndexTemp = i;
            
            for (int j = i + 1; j < citiesLength; j++) {
                if (temp[firstIndexTemp].temperature < temp[j].temperature) {
                    firstIndexTemp = j;
                }
            }
            
            if (firstIndexTemp != i) {
                int temperature_swap = temp[firstIndexTemp].temperature;
                temp[firstIndexTemp].temperature = temp[i].temperature;
                temp[i].temperature = temperature_swap;

                String city_swap = temp[firstIndexTemp].city;
                temp[firstIndexTemp].city = temp[i].city;
                temp[i].city = city_swap;
            }
        }
    }
}