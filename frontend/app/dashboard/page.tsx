"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import { tasksAPI, labelsAPI } from "@/lib/api";
import { Task, Label, TaskCreate, TaskUpdate } from "@/types";
import TaskCard from "@/components/TaskCard";
import TaskModal from "@/components/TaskModal";
import toast from "react-hot-toast";

export default function DashboardPage() {
  const { user, loading: authLoading, logout } = useAuth();
  const router = useRouter();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [labels, setLabels] = useState<Label[]>([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [filterLabel, setFilterLabel] = useState<string>("");
  const [filterCompleted, setFilterCompleted] = useState<string>("all");

  useEffect(() => {
    if (!authLoading && !user) {
      router.push("/login");
    }
  }, [user, authLoading, router]);

  useEffect(() => {
    if (user) {
      loadData();
    }
  }, [user, filterLabel, filterCompleted]);

  const loadData = async () => {
    try {
      const [tasksData, labelsData] = await Promise.all([
        tasksAPI.getAll(
          filterLabel || undefined,
          filterCompleted === "all" ? undefined : filterCompleted === "completed"
        ),
        labelsAPI.getAll(),
      ]);
      setTasks(tasksData);
      setLabels(labelsData);
    } catch (error) {
      console.error("Error loading data:", error);
      toast.error("Failed to load data");
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (data: TaskCreate) => {
    try {
      await tasksAPI.create(data);
      toast.success("Task created successfully!");
      loadData();
    } catch (error) {
      toast.error("Failed to create task");
      throw error;
    }
  };

  const handleUpdateTask = async (data: TaskUpdate) => {
    if (!editingTask) return;
    try {
      await tasksAPI.update(editingTask.id, data);
      toast.success("Task updated successfully!");
      loadData();
    } catch (error) {
      toast.error("Failed to update task");
      throw error;
    }
  };

  const handleDeleteTask = async (id: string) => {
    try {
      await tasksAPI.delete(id);
      toast.success("Task deleted successfully!");
      loadData();
    } catch (error) {
      toast.error("Failed to delete task");
    }
  };

  const handleToggleComplete = async (id: string, completed: boolean) => {
    try {
      await tasksAPI.update(id, { completed });
      loadData();
    } catch (error) {
      toast.error("Failed to update task");
    }
  };

  const handleEditTask = (task: Task) => {
    setEditingTask(task);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setEditingTask(null);
  };

  const handleOpenCreateModal = () => {
    setEditingTask(null);
    setIsModalOpen(true);
  };

  if (authLoading || loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 dark:border-blue-400"></div>
      </div>
    );
  }

  if (!user) {
    return null;
  }

  const completedCount = tasks.filter((t) => t.completed).length;
  const pendingCount = tasks.filter((t) => !t.completed).length;
  const overdueCount = tasks.filter(
    (t) => !t.completed && new Date(t.deadline) < new Date()
  ).length;

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 dark:text-white">My Tasks</h1>
              <p className="text-gray-600 dark:text-gray-300 mt-1">
                Welcome back, {user.full_name || user.email}!
              </p>
            </div>
            <button
              onClick={logout}
              className="px-4 py-2 text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition"
            >
              Logout
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400">Total Tasks</h3>
            <p className="text-3xl font-bold text-gray-900 dark:text-white mt-2">{tasks.length}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400">Pending</h3>
            <p className="text-3xl font-bold text-blue-600 dark:text-blue-400 mt-2">{pendingCount}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400">Completed</h3>
            <p className="text-3xl font-bold text-green-600 dark:text-green-400 mt-2">{completedCount}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 border border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400">Overdue</h3>
            <p className="text-3xl font-bold text-red-600 dark:text-red-400 mt-2">{overdueCount}</p>
          </div>
        </div>

        {/* Filters and Create Button */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4 mb-6 border border-gray-200 dark:border-gray-700">
          <div className="flex flex-wrap gap-4 items-center justify-between">
            <div className="flex flex-wrap gap-4 items-center">
              <div>
                <label htmlFor="filter-status" className="text-sm font-medium text-gray-700 dark:text-gray-300 mr-2">
                  Status:
                </label>
                <select
                  id="filter-status"
                  value={filterCompleted}
                  onChange={(e) => setFilterCompleted(e.target.value)}
                  className="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 outline-none bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
                >
                  <option value="all">All</option>
                  <option value="pending">Pending</option>
                  <option value="completed">Completed</option>
                </select>
              </div>
              <div>
                <label htmlFor="filter-label" className="text-sm font-medium text-gray-700 dark:text-gray-300 mr-2">
                  Label:
                </label>
                <select
                  id="filter-label"
                  value={filterLabel}
                  onChange={(e) => setFilterLabel(e.target.value)}
                  className="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 outline-none bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100"
                >
                  <option value="">All Labels</option>
                  {labels.map((label) => (
                    <option key={label.id} value={label.name}>
                      {label.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <button
              onClick={handleOpenCreateModal}
              className="px-6 py-2 bg-blue-600 dark:bg-blue-500 text-white rounded-lg hover:bg-blue-700 dark:hover:bg-blue-600 transition font-medium flex items-center gap-2"
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
                  d="M12 4v16m8-8H4"
                />
              </svg>
              Create Task
            </button>
          </div>
        </div>

        {/* Tasks List */}
        {tasks.length === 0 ? (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-12 text-center border border-gray-200 dark:border-gray-700">
            <svg
              className="w-16 h-16 text-gray-400 dark:text-gray-500 mx-auto mb-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
              />
            </svg>
            <h3 className="text-xl font-medium text-gray-900 dark:text-white mb-2">No tasks yet</h3>
            <p className="text-gray-600 dark:text-gray-300 mb-6">
              Get started by creating your first task!
            </p>
            <button
              onClick={handleOpenCreateModal}
              className="px-6 py-2 bg-blue-600 dark:bg-blue-500 text-white rounded-lg hover:bg-blue-700 dark:hover:bg-blue-600 transition font-medium"
            >
              Create Your First Task
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            {tasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onEdit={handleEditTask}
                onDelete={handleDeleteTask}
                onToggleComplete={handleToggleComplete}
              />
            ))}
          </div>
        )}
      </main>

      {/* Task Modal */}
      <TaskModal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        onSubmit={editingTask ? handleUpdateTask : handleCreateTask}
        task={editingTask}
        labels={labels}
      />
    </div>
  );
}
