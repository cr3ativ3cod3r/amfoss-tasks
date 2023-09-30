num = gets.to_i
 
 list=[2]
 
 for i in 3..num do
     a=0
     list.each do |j|
         if i%j!=0
             a+=1
         end
     end
    if a==list.length()
        list.append(i)
    end
        
 end
 
if num>=2
    puts list
end
