import React, { useState, useEffect } from 'react';
import { Plus, Check, Trash2, Edit3, Save, X } from 'lucide-react';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editText, setEditText] = useState('');
  const [filter, setFilter] = useState('all'); // all, active, completed

  // Load todos from localStorage on mount
  useEffect(() => {
    const savedTodos = localStorage.getItem('electron-todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  // Save todos to localStorage whenever todos change
  useEffect(() => {
    localStorage.setItem('electron-todos', JSON.stringify(todos));
  }, [todos]);

  const addTodo = () => {
    if (newTodo.trim()) {
      const todo = {
        id: Date.now(),
        text: newTodo.trim(),
        completed: false,
        createdAt: new Date().toISOString()
      };
      setTodos([todo, ...todos]);
      setNewTodo('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const startEdit = (id, text) => {
    setEditingId(id);
    setEditText(text);
  };

  const saveEdit = () => {
    if (editText.trim()) {
      setTodos(todos.map(todo =>
        todo.id === editingId ? { ...todo, text: editText.trim() } : todo
      ));
    }
    setEditingId(null);
    setEditText('');
  };

  const cancelEdit = () => {
    setEditingId(null);
    setEditText('');
  };

  const clearCompleted = () => {
    setTodos(todos.filter(todo => !todo.completed));
  };

  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true;
  });

  const completedCount = todos.filter(todo => todo.completed).length;
  const activeCount = todos.length - completedCount;

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      addTodo();
    }
  };

  const handleEditKeyPress = (e) => {
    if (e.key === 'Enter') {
      saveEdit();
    } else if (e.key === 'Escape') {
      cancelEdit();
    }
  };

  return (
    <div className="app">
      <div className="todo-container">
        <header className="header">
          <h1>Todo App</h1>
          <p>Built with Electron + React</p>
        </header>

        <div className="input-section">
          <div className="input-wrapper">
            <input
              type="text"
              value={newTodo}
              onChange={(e) => setNewTodo(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="What needs to be done?"
              className="todo-input"
            />
            <button onClick={addTodo} className="add-button">
              <Plus size={20} />
            </button>
          </div>
        </div>

        <div className="filter-section">
          <button
            className={`filter-btn ${filter === 'all' ? 'active' : ''}`}
            onClick={() => setFilter('all')}
          >
            All ({todos.length})
          </button>
          <button
            className={`filter-btn ${filter === 'active' ? 'active' : ''}`}
            onClick={() => setFilter('active')}
          >
            Active ({activeCount})
          </button>
          <button
            className={`filter-btn ${filter === 'completed' ? 'active' : ''}`}
            onClick={() => setFilter('completed')}
          >
            Completed ({completedCount})
          </button>
        </div>

        <div className="todos-section">
          {filteredTodos.length === 0 ? (
            <div className="empty-state">
              <p>
                {filter === 'all' ? 'No todos yet. Add one above!' :
                 filter === 'active' ? 'No active todos!' :
                 'No completed todos!'}
              </p>
            </div>
          ) : (
            <ul className="todo-list">
              {filteredTodos.map(todo => (
                <li key={todo.id} className={`todo-item ${todo.completed ? 'completed' : ''}`}>
                  <div className="todo-content">
                    <button
                      onClick={() => toggleTodo(todo.id)}
                      className={`complete-btn ${todo.completed ? 'completed' : ''}`}
                    >
                      {todo.completed && <Check size={16} />}
                    </button>
                    
                    {editingId === todo.id ? (
                      <input
                        type="text"
                        value={editText}
                        onChange={(e) => setEditText(e.target.value)}
                        onKeyPress={handleEditKeyPress}
                        className="edit-input"
                        autoFocus
                      />
                    ) : (
                      <span className="todo-text">{todo.text}</span>
                    )}
                  </div>
                  
                  <div className="todo-actions">
                    {editingId === todo.id ? (
                      <>
                        <button onClick={saveEdit} className="action-btn save">
                          <Save size={16} />
                        </button>
                        <button onClick={cancelEdit} className="action-btn cancel">
                          <X size={16} />
                        </button>
                      </>
                    ) : (
                      <>
                        <button
                          onClick={() => startEdit(todo.id, todo.text)}
                          className="action-btn edit"
                        >
                          <Edit3 size={16} />
                        </button>
                        <button
                          onClick={() => deleteTodo(todo.id)}
                          className="action-btn delete"
                        >
                          <Trash2 size={16} />
                        </button>
                      </>
                    )}
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        {completedCount > 0 && (
          <div className="footer-actions">
            <button onClick={clearCompleted} className="clear-completed">
              Clear Completed ({completedCount})
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;