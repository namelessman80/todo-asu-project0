"use client";

import { Task } from "@/types";
import { format } from "date-fns";
import { useState } from "react";

interface TaskCardProps {
  task: Task;
  onEdit: (task: Task) => void;
  onDelete: (id: string) => void;
  onToggleComplete: (id: string, completed: boolean) => void;
}

export default function TaskCard({ task, onEdit, onDelete, onToggleComplete }: TaskCardProps) {
  const [isDeleting, setIsDeleting] = useState(false);

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case "High":
        return "bg-red-100 dark:bg-red-900/30 text-red-800 dark:text-red-300 border-red-200 dark:border-red-800";
      case "Medium":
        return "bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-300 border-yellow-200 dark:border-yellow-800";
      case "Low":
        return "bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-300 border-green-200 dark:border-green-800";
      default:
        return "bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-300 border-gray-200 dark:border-gray-600";
    }
  };

  const handleDelete = async () => {
    if (window.confirm("Are you sure you want to delete this task?")) {
      setIsDeleting(true);
      try {
        await onDelete(task.id);
      } catch (error) {
        setIsDeleting(false);
      }
    }
  };

  const isOverdue = new Date(task.deadline) < new Date() && !task.completed;

  return (
    <div
      className={`bg-white dark:bg-gray-800 rounded-lg shadow-md border border-gray-200 dark:border-gray-700 p-4 hover:shadow-lg transition ${
        task.completed ? "opacity-60" : ""
      } ${isDeleting ? "opacity-50" : ""}`}
    >
      <div className="flex items-start gap-3">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={(e) => onToggleComplete(task.id, e.target.checked)}
          className="mt-1 h-5 w-5 text-blue-600 dark:text-blue-500 rounded focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600"
        />
        <div className="flex-1">
          <h3
            className={`text-lg font-semibold text-gray-900 dark:text-white ${
              task.completed ? "line-through" : ""
            }`}
          >
            {task.title}
          </h3>
          {task.description && (
            <p className="text-gray-600 dark:text-gray-300 mt-1 text-sm">{task.description}</p>
          )}
          <div className="flex flex-wrap gap-2 mt-3">
            <span
              className={`text-xs px-2 py-1 rounded-full border font-medium ${getPriorityColor(
                task.priority
              )}`}
            >
              {task.priority}
            </span>
            <span
              className={`text-xs px-2 py-1 rounded-full font-medium ${
                isOverdue
                  ? "bg-red-100 dark:bg-red-900/30 text-red-800 dark:text-red-300 border border-red-200 dark:border-red-800"
                  : "bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-300 border border-blue-200 dark:border-blue-800"
              }`}
            >
              {format(new Date(task.deadline), "MMM dd, yyyy")}
            </span>
            {task.labels.map((label, index) => (
              <span
                key={index}
                className="text-xs px-2 py-1 rounded-full bg-purple-100 dark:bg-purple-900/30 text-purple-800 dark:text-purple-300 border border-purple-200 dark:border-purple-800 font-medium"
              >
                {label}
              </span>
            ))}
          </div>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => onEdit(task)}
            className="text-blue-600 dark:text-blue-400 hover:text-blue-800 dark:hover:text-blue-300 p-1"
            title="Edit task"
          >
            <svg
              className="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
              />
            </svg>
          </button>
          <button
            onClick={handleDelete}
            disabled={isDeleting}
            className="text-red-600 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300 p-1 disabled:opacity-50"
            title="Delete task"
          >
            <svg
              className="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
}
