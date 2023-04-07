-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- Note: An average score can be a decimal
-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(5, 2);
    DECLARE num_corrections INT;
    DECLARE avg_score DECIMAL(5, 2);
    
    SELECT SUM(score), COUNT(*) INTO total_score, num_corrections
    FROM corrections
    WHERE user_id = user_id;
    
    IF num_corrections > 0 THEN
        SET avg_score = total_score / num_corrections;
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    ELSE
        UPDATE users SET average_score = NULL WHERE id = user_id;
    END IF;
END //

DELIMITER ;
