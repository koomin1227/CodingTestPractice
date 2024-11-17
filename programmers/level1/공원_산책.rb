def find_start_point(park)
    for i in 0..park.length - 1
        for j in 0..park[0].length - 1
            return [i,j] if park[i][j] == 'S'
        end
    end
end

def solution(park, routes)    
    direction_number = {"E"=> 0, "N"=> 1, "W"=> 2, "S"=> 3}
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    current_position = find_start_point(park)
    
    routes.each { |route|
        is_movable = true
        direction, n = route.split " "
        next_y = current_position[0] + dy[direction_number[direction]] * n.to_i
        next_x = current_position[1] + dx[direction_number[direction]] * n.to_i
        if next_y < 0 || next_y >= park.length || next_x < 0 || next_x >= park[0].length
            next
        end
        
        1.upto n.to_i do |i|
            y = current_position[0] + dy[direction_number[direction]] * i
            x = current_position[1] + dx[direction_number[direction]] * i
            
            is_movable = false if park[y][x] == 'X'
        end
        
        if is_movable
            current_position[0] = next_y
            current_position[1] = next_x
        end
        
    }
    return current_position
end